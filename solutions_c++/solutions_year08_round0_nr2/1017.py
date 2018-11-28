#include<stdio.h>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>

using namespace std;

int N, NA, NB, T, START_A, START_B;

int convert(const char * str){
    int out = 0;
    out += (str[0]-'0')*600;
    out += (str[1]-'0')*60;
    out += (str[3]-'0')*10;
    out += (str[4]-'0');
    return out;
}

char start[256], stop[256];

int main()
{
    scanf("%d", &N);
    for(int tc=1;tc<=N;++tc)
    {
        scanf("%d", &T);
        scanf("%d%d", &NA, &NB);
        
        vector< pair< pair<int, int>, char > > V;
        for(int i=0;i<NA;i++){
            scanf("%s %s\n", start, stop);
            V.push_back( make_pair( make_pair(convert(start), convert(stop)), 'A'));
        }
        for(int i=0;i<NB;i++){
            scanf("%s %s\n", start, stop);
            V.push_back( make_pair( make_pair(convert(start), convert(stop)), 'B'));
        }
        
        sort(V.begin(), V.end());
        //printf("NA = %d, NB = %d\n", NA, NB);
        if(NA==0 || NB==0)
            printf("Case #%d: %d %d\n", tc, NA, NB);
        else{
            int OK;
            for(int sum=1;sum<=(NA+NB);sum++){
                //printf("sum = %d\n", sum);
                for(START_A=0;START_A<=sum;START_A++){
                    START_B = sum - START_A;
                    //printf("%d %d\n", START_A, START_B);
                    multiset<int> READY_A, READY_B;
                    for(int i=0;i<START_A;i++)READY_A.insert(0);
                    for(int i=0;i<START_B;i++)READY_B.insert(0);
                    //invariant START_A + START_B = sum
                    OK = 1;
                    for(int i=0;i<V.size();i++){
                        /*
                        printf("\t i = %d   ( (%d,%d), %c )\n", i, V[i].first.first, V[i].first.second, V[i].second);
                        printf("\t\tREADY_A : ");
                        for(multiset<int>::iterator iter=READY_A.begin();iter!=READY_A.end();iter++){
                            printf("%d ", *iter);
                        }
                        printf("\n");
                        
                        printf("\t\tREADY_B : ");
                        for(multiset<int>::iterator iter=READY_B.begin();iter!=READY_B.end();iter++){
                            printf("%d ", *iter);
                        }
                        printf("\n");
                        */
                        char ch = V[i].second;
                        if(ch=='A'){
                            if(READY_A.empty() || *(READY_A.begin())>V[i].first.first){
                                //printf("here!\n");
                                OK = 0;break;
                            } else{
                                READY_A.erase(READY_A.begin());
                                READY_B.insert(V[i].first.second + T);
                            }
                        }else{
                            if(READY_B.empty() || *(READY_B.begin())>V[i].first.first){
                                //printf("here\n");
                                OK = 0;break;
                            } else{
                                READY_B.erase(READY_B.begin());
                                READY_A.insert(V[i].first.second + T);
                            }
                        }
                    }
                    //printf("now here!\n");
                    if(OK){
                        printf("Case #%d: %d %d\n", tc, START_A, START_B);
                        break;
                    }
                }
                //printf("OK = %d\n", OK);
                if(OK)break;
            }
        
            
        }
            
        
    }
    return 0;
}
