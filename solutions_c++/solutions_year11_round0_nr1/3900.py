#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int caseNum=1;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");
	int cnt;
	fin >> cnt;//////////
	while(cnt-- > 0)
	{
		int num;
		fin >> num;
		int blue = 1; //blue�ĵ�ǰλ��
		int orange = 1;//orange�ĵ�ǰλ��
		int place; //b��o����һ��λ��
		char R='T'; //�ĸ�robot
		char preR;
		int sec=0;
		int span=0; //��һ����ʱ����
		int tmp;
		while(num-- > 0)
		{
			preR=R;
			fin >> R;
			fin >> place;
			if(preR!=R)
			{
				if(R=='B')
				{
					tmp = place-blue;
					if(tmp<0)
						tmp=-tmp;
					if(tmp<span)
						span=1;
					else
						span=tmp-span+1;
					blue=place;
				}
				else
				{
					tmp = place-orange;
					if(tmp<0)
						tmp=-tmp;
					if(tmp<span)
						span=1;
					else
						span=tmp-span+1;
					orange=place;
				}
				sec += span;
			}
			else
			{
				if(R=='B')
				{
					tmp=place-blue;
					if(tmp<0)
						tmp=-tmp;
					sec+=tmp+1;
					span+=tmp+1;
					blue=place;
				}
				else
				{
					tmp=place-orange;
					if(tmp<0)
						tmp=-tmp;
					sec+=tmp+1;
					span+=tmp+1;
					orange=place;
				}
			}
		}
		fout << "Case #" << caseNum++ << ": " << sec << endl;
	}
} 