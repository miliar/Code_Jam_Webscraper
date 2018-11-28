# include <iostream>
# include <Vector>
# include <string>
# include <stdio.h>
using namespace std;
int main()
{
    int N;
    cin>>N;
    for(int z=0;z<N;z++)
    {
            int S,Q;string en;
            vector<string> eng,que;
            vector<int> map;
            cin>>S;
            char st[100];
            fflush(stdin);
            for(int i=0;i<S;i++)
                    {scanf("%[^\n]",st);fflush(stdin);en=st;eng.push_back(en);map.push_back(0);}
            cin>>Q;
            fflush(stdin);
            for(int i=0;i<Q;i++)
                    {scanf("%[^\n]",st);fflush(stdin);en=st;que.push_back(en);}
            int sw=0;
            for(int i=0;i<Q;i++)
            {
                    int p=-1;
                    for(int j=0;j<S;j++)
                    {
                            if(eng[j]==que[i]) 
                            {map[j]=1;p=j;break;}
                    }
                    int fg=0;
                    for(int j=0;j<map.size();j++)
                            if(map[j]==0) {fg=1;break;}
                    if(fg==0)
                    {
                             for(int j=0;j<map.size();j++)
                                     map[j]=0;
                             map[p]=1;
                             sw++;        
                    }
                    
            }
            cout<<"Case #"<<z+1<<": "<<sw<<"\n";
    }
    return 0;
}
