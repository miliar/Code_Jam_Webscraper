#include <iostream>
#include <cstdio>

using namespace std;

long long n;
int Pd,Pg;
int T;

int main(){
    cin>>T;
    for (int caseID = 1; caseID <= T; caseID++){
        printf("Case #%d: ", caseID);
        cin>>n>>Pd>>Pg;
        if (n >= 100ll){
            if (Pg == 100 && Pd < 100) printf("Broken\n");
                else if (Pg == 0 && Pd > 0) printf("Broken\n");
                else printf("Possible\n");
        }else{
            bool can = false;
            for (int testn  = 1; testn <= (int)n; testn++){
                if ((testn*Pd)%100 == 0){
                    can = true;
                    break;
                }
            }
            if (!can) printf("Broken\n");
            else{
                if (Pg == 100 && Pd < 100) printf("Broken\n");
                else if (Pg == 0 && Pd > 0) printf("Broken\n");
                else printf("Possible\n");
            }
        }
    }    
}
