#include<iostream>
using namespace std;
int main()
{
    int tab[110];
    int googlers,t,special,minimal,score,res,used,x;
    cin >> t;
    for(int i=1; i<=t; i++) {
        cin >> googlers >> special >> minimal;
        res=0;
        for(int j=0; j<googlers; j++) {
            cin >> score;
            used=0;
            if(minimal>0) {
                if((score%3==0)&&(score>=0)) {
                    x=score/3;
                    if(x>=minimal) {
                        res++;
                        used=1;
                    }
                }
                else if((score%3==1)&&(score>=1)) {
                    x=(score-1)/3;
                    if(x+1>=minimal) {
                        res++;
                        used=1;
                    }
                }
                else if((score%3==2)&&(score>=2)) {
                    x=(score-2)/3;
                    if(x+1>=minimal) {
                        res++;
                        used=1;
                    }
                }
                if((used==0)&&(special>0)) {
                    if(score%3==0) {
                        x=(score-3)/3;
                        if((x+2>=minimal)&&(score>=3)){
                            special--;
                            res++;
                        }
                    }
                    else if((score%3==2)&&(score>=2)) {
                        x=(score-2)/3;
                        if(x+2>=minimal) {
                            special--;
                            res++;
                        }
                    }
                    else if((score%3==1)&&(score>=4)) {
                        x=(score-4)/3;
                        if(x+2>=minimal) {
                            special--;
                            res++;
                        }
                    }
                }
            }
            else {
                res=googlers;
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }
}
