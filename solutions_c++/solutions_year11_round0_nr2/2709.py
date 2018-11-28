#include <cstdio>
#include <cstring>
//#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;
#define MAXN 128
char map[1024];
char opp[32];
char input[MAXN];
string result;
int main()
{
    int T,C,D,N,round=1;
    scanf("%d",&T);
    while(T--)
    {
        for(int i=0;i<1024;i++) map[i]=0;
        for(int i=0;i<32;i++) opp[i]=0;
        result.clear();
        scanf("%d",&C);
        char str[4];
        while(C--)
        {
            scanf("%s",str);
            int first=(str[0]-'A')*26+(str[1]-'A');
            int second=(str[1]-'A')*26+(str[0]-'A');
            map[first]=map[second]=str[2];
        }
        scanf("%d",&D);
        while(D--)
        {
            scanf("%s",str);
            opp[str[0]-'A']=str[1];
            opp[str[1]-'A']=str[0];
        }
        scanf("%d",&N);
        scanf("%s",input);
        for(int i=0;i<N;i++)
        {
            result.push_back(input[i]);
        }
        for(string::iterator iter=result.begin();iter!=result.end();)
        {
            if(iter==result.begin())
            {
                iter++;
                if(iter==result.end()) break;
            }
            string::iterator tmpIter=iter;
            tmpIter--;
            bool found=false;
            //check merge
            int val=(*tmpIter-'A')*26+*iter-'A';
            if(map[val]!=0)
            {
                tmpIter=result.erase(tmpIter);
                tmpIter=result.erase(tmpIter);
                iter=result.insert(tmpIter,map[val]);
                found=true;
            }
            if(found) continue;
            tmpIter=iter;
            //check oppose
            bool found2=false;
            if(tmpIter==result.begin()) continue;
            while(--tmpIter!=result.begin())
            {
//                tmpIter--;
                string::iterator nextIter=iter;
                nextIter++;
                if(opp[*tmpIter-'A']==*iter)
                {
                    iter=result.erase(result.begin(),nextIter);
                    found2=true;
                    break;
                }
            }
            if(!found2&&(tmpIter==result.begin()))
            {
                 if(opp[*tmpIter-'A']==*iter)
                {
                    string::iterator nextIter=iter;
                    nextIter++;
                    iter=result.erase(result.begin(),nextIter);
//                    iter=tmpIter;
                    found2=true;
                }
            }
//            bool found2=false;
            if(!found2) iter++;
        }
        printf("Case #%d: [",round++);
        for(string::iterator iter=result.begin();iter!=result.end();iter++)
        {
            cout<<*iter;
            string::iterator tmpIter=iter;
            if(++tmpIter!=result.end()) cout<<", ";
        }
        printf("]\n");
    }
//    system("pause");
    return 0;
}
