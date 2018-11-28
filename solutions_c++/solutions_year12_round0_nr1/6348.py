#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	 ofstream outfile("data.out",ios::out);
	char temp[200]={0};
	char translate[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	char translate1[26]={0};
	int t,i,j;
	for(i=0;i<26;i++)
	{
		for(j=0;j<26;j++)if(translate[j]==i+'a')break;
        translate1[i]=j+'a';
	}

	cin>>t;cin.getline(temp,200);
	for(i=0;i<t;i++)
	{int j,str_len;
			
	


			cin.getline(temp,200);
			str_len=strlen(temp);
			for(j=0;j<str_len;j++)
			{
				if(temp[j]>='a'&&temp[j]<='z')
				{
				temp[j]=translate1[temp[j]-'a'];
			    
				}
			}
					outfile<<"Case #";
			outfile<<i+1; 
			outfile<<": ";
			outfile<<temp;
			outfile<<endl;
	}
	
	return 0;
}