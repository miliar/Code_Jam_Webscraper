#include<iostream>
#include<fstream>
using namespace std;

char a[]="vprtwfceokidsnbhxmlgvjujayazqz";

int main()
{
	ofstream fout("ans.txt");
	int input;
	char A[10];
	cin>>input;
	cin.getline(A,10);
	int out=1;
	while(input>0)
	{
		char G[101];
		cin.getline(G,101);
		fout<<"Case #"<<out<<": ";
		out++;
		for(int i=0;i<strlen(G);i++)
		{
			if(G[i]==' ')
			{
				fout<<" ";
			}
			else
			{
				for(int j=0;j<30;j++)
				{
					if(G[i]==a[j])
					{
						fout<<a[j+1];
						break;
					}
				}
			}
		}
		fout<<endl;
		input--;
	}
}