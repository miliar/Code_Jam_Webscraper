//#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int Googler[101];
void Read()
{
	
    ifstream fin("B-large.in"); 
	ofstream f("B-large.out");
	int n;
	int sum=0;
	fin>> n;
	int N,S,P;
	for(int i=0;i<n;i++)
    {    
		fin>>N>>S>>P;
        f<<"Case #"<<i+1<<": ";
		for(int j=0;j<N;j++)
		{
			fin>>Googler[j];
		}
		//≈≈–Ú
		for(int i=0;i< N;i++)
			for(int j=0;j< N-i-1;j++)
			{
				if(Googler[j]<Googler[j+1])
				{
					int temp;
					temp=Googler[j];
					Googler[j]=Googler[j+1];
					Googler[j+1]=temp;
				}
			}
	
			/*for(int i=0;i<N;i++)
				f<<Googler[i]<<" ";*/
			for(int i=0;i<N;i++)
			{
				if((0==Googler[i]%3&&Googler[i]/3>=P)||(0!=Googler[i]%3&&Googler[i]/3+1>=P))//(Googler[i]/3+1>=P&&Googler[i]%3!=0&&Googler[i]/3+1!=P)//(Googler[i]/3+1>P&&Googler[i]%3!=0) ||
				{
					sum++;
					continue;
				}
				else
				{
					//∑÷«Èøˆ≈–∂œ
					//surprising
					if(Googler[i]==0&&P!=0)
						continue;
					else if( 0==Googler[i]%3 && Googler[i]/3+1>=P  && S!=0)
					{
						sum++;
						S--;
					}
					//surprising
					else if(1==Googler[i]%3 && Googler[i]/3+1 >=P && S!=0)
					{
						sum++;
						S--;
					}
					//surprising
					else if(2==Googler[i]%3 && Googler[i]/3+2>=P && S!=0)
					{
						sum++;
						S--;
					}
				/*	else if(N-1==i  && S>0)
						sum+=S;
*/
				
				}
			}
				f<<sum;
				sum=0;
				f<<endl;
    }
	
}

int main()
{
	Read();
	//system("pause");
	return 0;
}