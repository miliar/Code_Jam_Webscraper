#include <iostream>
#include <string>
using namespace std;
int main()
{
    int L,D,N;
    scanf("%d%d%d",&L,&D,&N);
    char words[5100][30];
    for(int i=0;i<D;i++)
        scanf("%s",words[i]);
        
            
    char keys[30][30];
    for(int T=1;T<=N;T++)
    {
        memset(keys,0,sizeof(keys));
        char t[10000];
        scanf("%s",t);
        int p=0;
        for(int i=0;i<L;i++)
        {
            if(t[p]=='(')
            {
                 while(1)
                 {
                     p++;
                     if(t[p]==')'){p++; break;}
                     keys[i][t[p]-'a']=1;
                 }
            }
            else
            {
                keys[i][t[p]-'a']=1;
                p++;
            }                                                     
        }
        int total=0;
        for(int i=0;i<D;i++)
        {
			int flag=1;
			for(int j=0;j<L;j++)
			{
				if(keys[j][words[i][j]-'a']==0)
				{
					flag=0;
					break;
				}
			}
			total += flag;
		}
		
        cout<<"Case #"<<T<<": "<<total<<endl;
            
    }
    
            

}
