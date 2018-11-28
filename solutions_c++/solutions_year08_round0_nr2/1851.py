#include <cstdio>
#include <vector>
using namespace std;

struct Time{
    int Hour;
    int Min;
};

vector <Time *> BeginT;
vector <Time *> ArriveT;
int NA,NB,T;
int NumA,NumB;
vector <Time *>::iterator ite;
vector <Time *>::iterator ite1;
//vector <Time *>::iterator ite2;
//vector <Time *>::iterator ite3;

void UpdateArriveTime(){
    for(ite = ArriveT.begin(); ite != ArriveT.end(); ++ite){
        (*ite)->Min += T;
        if((*ite)->Min > 59){
            (*ite)->Min -= 60;
            (*ite)->Hour++;
            if((*ite)->Hour > 23){
                (*ite)->Hour = 0;
            }
        }
    }
}

void Sort(vector <Time *>::iterator IteBegin,vector <Time *>::iterator IteEnd){
    for(ite = IteBegin; ite != IteEnd; ++ite){
        for(ite1 = IteBegin; ite1 < ite; ++ite1){
            Time * tmp;
            bool IsTrue = false;
            if((*ite)->Hour < (*ite1)->Hour){
                IsTrue = true;
            }else if((*ite)->Hour == (*ite1)->Hour){
                if((*ite)->Min < (*ite1)->Min){
                    IsTrue = true;
                }
            }
            if(IsTrue){
                tmp = (*ite);
                (*ite) = (*ite1);
                (*ite1) = tmp;
                //int z = (int) (ite - ArriveT.begin());
                //ite2 = BeginT.begin() + z;
                //z = (int) (ite1 - ArriveT.begin());
                //ite3 = BeginT.begin() + z;
                //tmp = (*ite2);
                //(*ite2) = (*ite3);
                //(*ite3) = tmp;
            }
        }
    }
}

void SortTime(){
    ite = ArriveT.begin();
    ite1 = ArriveT.begin() + NA;
    Sort(ite,ite1);
    ite = ArriveT.end();
    Sort(ite1 + 1,ite);
}

int FindSolution(){
    //for(ite = ArriveT.begin(); ite != ArriveT.end(); ++ite){
    //    printf("aaa%d:%d\n",(*ite)->Hour,(*ite)->Min);
    //}
    NumA = NA;
    NumB = NB;
    for(ite = BeginT.begin(); ite != BeginT.begin() + NA; ++ite){
        //printf("dfdfdf%d:%d\n",(*(ArriveT.begin() + NA))->Hour,(*(ArriveT.begin() + NA))->Min);
        for(ite1 = ArriveT.end() - 1; ite1 != ArriveT.begin() + NA - 1; --ite1){
            bool IsTrue = false;
            if((*ite)->Hour > (*ite1)->Hour){
                IsTrue = true;
            }else if((*ite)->Hour == (*ite1)->Hour){
                if((*ite)->Min >= (*ite1)->Min){
                    IsTrue = true;
                }
            }
            if(IsTrue){
                //printf("%d:%d\t%d:%d\t%d\n",(*ite)->Hour,(*ite)->Min,(*ite1)->Hour,(*ite1)->Min,ite - BeginT.begin());
                /*int z = (int) (ite1 - ArriveT.begin());
                ite2 = BeginT.begin() + z;
                z = (int) (ite - BeginT.begin());
                ite3 = (ArriveT.begin() + z);
                bool IsF = false;
                if((*ite2)->Hour > (*ite3)->Hour){
                    IsF =true;
                }else if((*ite2)->Hour == (*ite3)->Hour){
                    if((*ite2)->Min >= (*ite)->Min){
                        IsF = true;
                    }
                }
                if(IsF){*/
                    NumA--;
                    (*ite1)->Hour = 25;
                    break;
                //}
            }
        }
    }
    //printf("A Completed\n");
    for(ite = BeginT.begin() + NA; ite != BeginT.end(); ++ite){
        ite1 = ArriveT.begin();
        //printf("dfdfdf%d:%d\n",(*ite1)->Hour,(*ite1)->Min);        
        for(ite1 = ArriveT.begin() + NA - 1; ite1 != ArriveT.begin() - 1; --ite1){
            bool IsTrue = false;
            if((*ite)->Hour > (*ite1)->Hour){
                IsTrue = true;
            }else if((*ite)->Hour == (*ite1)->Hour){
                if((*ite)->Min >= (*ite1)->Min){
                    IsTrue = true;
                }
            }
            if(IsTrue){
                //printf("%d:%d\t%d:%d\t%d\n",(*ite)->Hour,(*ite)->Min,(*ite1)->Hour,(*ite1)->Min,ite - BeginT.begin());
                /*int z = (int) (ite1 - ArriveT.begin());
                ite2 = BeginT.begin() + z;
                z = (int) (ite - BeginT.begin());
                ite3 = (ArriveT.begin() + z);
                bool IsF = false;
                if((*ite2)->Hour > (*ite3)->Hour){
                    IsF =true;
                }else if((*ite2)->Hour == (*ite3)->Hour){
                    if((*ite2)->Min >= (*ite)->Min){
                        IsF = true;
                    }
                }
                if(IsF){*/
                    NumB--;
                    (*ite1)->Hour = 25;
                    break;
                //}
            }
        }
    }
    return 0;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int IntCases;
    scanf("%d",&IntCases);
    for(int i = 0; i < IntCases; ++i){
        BeginT.clear();
        ArriveT.clear();
        scanf("%d",&T);
        scanf("%d %d",&NA,&NB);
        Time * tmp;
        for(int k = 0; k < NA + NB; ++k){
            int BeginHour,BeginMin;
            int ArriveHour,ArriveMin;
            scanf("%d:%d %d:%d",&BeginHour,&BeginMin,&ArriveHour,&ArriveMin);
            tmp = (Time *) new Time;
            tmp->Hour = BeginHour;
            tmp->Min =  BeginMin;
            BeginT.push_back(tmp);
            tmp = (Time *) new Time;
            tmp->Hour = ArriveHour;
            tmp->Min = ArriveMin;
            ArriveT.push_back(tmp);
        }
        UpdateArriveTime();
        SortTime();
        FindSolution();
        if(!NA){
            NumA = 0;
        }
        if(!NB){
            NumB = 0;
        }
        printf("Case #%d: %d %d\n",i + 1,NumA,NumB);
    }
    return 0;
}

