#include<iostream>
#include<string>
using namespace std;

int L,D,N,i;
int count[505] = {0};
int bracket = 0;
int c2 = 0;
bool xyz, m1;

char words[5005][25];

char msg[600];
string s[16];


int main()
{
cin>>L>>D>>N;

for( i = 1 ; i <= D ; i++)
        scanf("%s",words[i]);

for( i = 1 ; i <=N ; i++)
{        
        scanf("%s", msg);      
        count[i] = 0;
        
        c2 = -1;
        bracket = 0;
        
        for(int t = 0; t<=15;t++)
                s[t] = "\0";     
                
                
        for(int t = 0; msg[t]!= '\0'; t++)
        {
                if(msg[t] == '(')
                {
                        bracket = 1;
                        c2++;    
                }
                else if(msg[t] == ')')
                {
                        bracket = 0;
                }                
                else if(!bracket)
                {
                        
                        c2++;
                        s[c2] = s[c2] + msg[t];
                }   
                else
                {
                        s[c2] = s[c2] + msg[t];
                }
                        
        }                             
                    
        for(int j = 1 ; j <= D ; j++)
        {
                xyz = true;
                for(int k = 1; k<= L; k++)
                {
                        m1 = false;
                        for(int x = 0 ; s[k-1][x] != '\0' ; x++)
                                if(words[j][k-1] == s[k-1][x])
                                        m1 = true;
                                        
                        if(m1 == false)
                        {
                                xyz = false;
                                break;
                        }                
                }
                if(xyz)
                        count[i]++;                              
        }
                                
} 
for( i = 1 ; i<=N; i++)
        cout<<"Case #"<<i<<": "<<count[i]<<endl;

}


