#include <iostream>
#include <fstream>
using namespace std;

char str[101];

int main()
{
	str[100]='\0';
	ifstream fin("B-small-attempt3.in");
	ofstream fout("B-small.out");
	int cnt;
	fin >> cnt;
	int caseNum=0;
	while(cnt-- > 0)
	{
		int C,D,N;
		int combine[26][26]={0}; //eg. combine[0][1]=3代表AB组合成C; combine=0代表不组合
		int oppose[26]={0}; //代表敌对的字符 eg. oppose[0]=2，代表A的敌对为B, oppose为0代表不敌对
		int oppose_list[26]={0}; //代表当前list，出现字符，就敌对的。eg. oppose_list[0]=1代表出现A就clear list，0代表不出现
		
		char tmp1,tmp2,tmp3;

		fin >> C;
		while(C-- > 0)
		{
			fin >> tmp1 >> tmp2 >> tmp3;
			combine[tmp1-'A'][tmp2-'A']=tmp3-'A'+1;
			combine[tmp2-'A'][tmp1-'A']=tmp3-'A'+1;
		}
		fin >> D;
		while(D-- > 0)
		{
			fin >> tmp1 >> tmp2;
			oppose[tmp1-'A']=tmp2-'A'+1;
			oppose[tmp2-'A']=tmp1-'A'+1;
		}
		fin >> N;
		for(int k=0;k<101;k++)
			str[k]='0';

		char cc;
		int j=0;
		bool is_list_empty=true;
		for(int i=0;i<N;i++)
		{
			fin >> cc;
			if(is_list_empty)
			{
				is_list_empty=false;
				j=0;
				str[j]=cc;
				if(oppose[cc-'A']!=0)
					oppose_list[oppose[cc-'A']-1]++;
			}
			else
			{
				char precc=str[j];
				if(combine[cc-'A'][precc-'A']!=0)
				{
					str[j]='A'+combine[cc-'A'][precc-'A']-1;
					if(oppose[str[j]-'A']!=0)
						oppose_list[oppose[str[j]-'A']-1]++;
					if(oppose[precc-'A']!=0)
						oppose_list[oppose[precc-'A']-1]--;

				}
				else
				{
					str[++j]=cc;
					if(oppose_list[cc-'A']!=0)
					{
						j=0;
						is_list_empty=true;
						for(int k=0;k<100;k++)
							str[k]='0';
						for(int k=0;k<26;k++)
							oppose_list[k]=0;
					}
					else
					{
						if(oppose[cc-'A']!=0)
							oppose_list[oppose[cc-'A']-1]++;
					}
				}
			}
		}
		fout << "Case #" << ++caseNum << ": [";
		int k=0;
		while(str[k]!='0')
		{
			fout << str[k];
			k++;
			if(str[k]!='0' && k!=100)
				fout << ", ";
		}
		fout << "]" << endl;
	}
	
}