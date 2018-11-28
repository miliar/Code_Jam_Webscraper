
#include <iostream>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <algorithm>
#include <set>
using namespace std;
       

bool special_sort(int x,int y)
{
    return x > y;
}
inline bool isSpecial(int &x,int &count)
{
    if(count>0) {
        if( (x%3==0||x%3==2) && (x>1&&x<28))
        {
            return true;
        } else {
            return false;
        }
    }
    return false;
}
typedef unsigned long ll;

int main(int argc,char *argv[])
{
    int testCaseCount;
    cin >> testCaseCount;
    for(int testCase=1;testCase<=testCaseCount;testCase++)
    {
        int scoreCount;
        cin >> scoreCount;

        int specialCount;
        cin >> specialCount;

        int maxScore;
        cin >> maxScore;

        int val;
        int ret=0;
        vector<int> x;
        for(int i=0;i<scoreCount;i++) {
            cin >> val;
            x.push_back(val);
        }
        sort(x.begin(),x.end(),special_sort);
        
        int sc=specialCount;

        for(int i=0;i<scoreCount;i++) {
            if( isSpecial(x[i],sc) ) {
                sc-- ;
                
                if((x[i]%3==0 && (x[i]/3)+1 >=maxScore)) 
                {
                    if((x[i]!=0)||(maxScore==0)) 
                        ret++;
                }
                else if((x[i]%3==2 && ((x[i]/3)+2 >=maxScore)))
                    ret++;
            } else {
                if( x[i]%3==0 ){
                    if(x[i]/3>=maxScore)
                        ret++;
                }
                else if( ((x[i]/3)+1)>=maxScore )
                {
                    if(x[i]!=0 || maxScore==0) {
                        ret++;
                    }
                }
            }

        }

        sc = specialCount;
        int revRet=0;
        reverse(x.begin(),x.end());
        for(int i=0;i<scoreCount;i++) {
            if( isSpecial(x[i],sc) ) {
                sc-- ;
                
                if((x[i]%3==0 && (x[i]/3)+1 >=maxScore)) 
                {
                    if((x[i]!=0)||(maxScore==0)) 
                        revRet++;
                }
                else if((x[i]%3==2 && ((x[i]/3)+2 >=maxScore)))
                    revRet++;
            } else {
                if( x[i]%3==0 ){
                    if(x[i]/3>=maxScore)
                        revRet++;
                }
                else if( ((x[i]/3)+1)>=maxScore )
                {
                    if(x[i]!=0 || maxScore==0) {
                        revRet++;
                    }
                }
            }
        }

        
        cout << "Case #"<< testCase << ": " << max(ret,revRet) << endl;
    }
    return 0;
}
