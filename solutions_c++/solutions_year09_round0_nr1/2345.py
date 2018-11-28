#include <iostream>
#include <string>

using namespace std;
using std::string;

int L, D, N;


int main()
{   
    cin >> L >> D >> N;
    string lost;
    getline(cin,lost);
   

    string dico[5000];
    for(int i=0;i<D;i++)
	{
	    getline(cin,dico[i]);
	}
    string pattern[500];
    for(int i=0;i<N;i++)
	{
	    getline(cin,pattern[i]);
	}
    int counter[500];
    for(int i=0;i<N;i++)
	{
	    counter[i]=0;
	}
    

    for(int i=0;i<D;i++)
	{
	    for(int j=0;j<N;j++)
		{
		    int m=0;
		    int k=0;
		    int ok = 1; 
		    while(k < L && ok == 1)
			{
			    if(pattern[j][m]==dico[i][k])
				{
				    m++;
				    k++;
				}

			    else
				{
				    if(pattern[j][m]!='(')
					{
					    ok = 0;
					}
				    else
					{
					    m++;
					    int localok = 0;
					    while(pattern[j][m] !=')')
						{
						    if(pattern[j][m] == dico[i][k])
							{
							    localok = 1;
							}
						    m++;
						}
					    m++;
					    if(localok == 0)
						{
						    ok = 0;
						}
					    else
						{
						    k++;
						}
					}
				}
			}
		    if(k==L)
			{
			    counter[j] = counter[j] + 1;
			}    
		}    
	}
    for(int j=0;j<N;j++)
	{
	    cout << "Case #" << j+1 << ": " << counter[j] << endl;
	}
}
