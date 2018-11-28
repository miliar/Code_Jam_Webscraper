#include<stdio.h>
#include<memory.h>

int main(){
    freopen("input2.in","r",stdin);
    freopen("output2_lib.txt","w",stdout);

    int t=0;
    scanf("%d" ,&t);

    //int score[100];
    int i=0;
    for(i=0;i<t;i++){
        int n,s,p;
        scanf("%d %d %d ",&n, &s,&p);
        ///////init down
        int iter=0;
        int add=0,minus=0,eq=0;
        int result=0;
        for(iter=0;iter<n;iter++){
            //scanf("%d",&(score[iter]));
            int temp=0;
            scanf("%d",&temp);
            int given=0,ungiven=0;

            if(temp%3==0){
                int a=temp/3;
                if(a>=p&&a>=0){
                    ungiven=1;
                }
            }

            if((temp-1)%3==0){
                int a=(temp-1)/3;
                if(a+1>=p&&a>=0){
                    ungiven=1;
                }
            }

            if((temp-2)%3==0){
                int a=(temp-2)/3;
                if(a+2>=p&&a>=0){
                    given=1;
                }
                if(a+1>=p&&a>=0){
                    ungiven=1;
                }
            }

            if((temp-4)%3==0){
                int a=(temp-4)/3;
                if(a+2>=p&&a>=0){
                    given=1;
                }
            }

            if((temp-3)%3==0){
                int a=(temp-3)/3;
                if(a+2>=p&&a>=0){
                    given=1;
                }
            }
            ////////six possible compute end, check the iter to result
            if(given==1&&ungiven==0){
                add++;
            }
            else if(given==0&&ungiven==1){
                minus++;
                result++;
            }
            else if(given==0&&ungiven==0){
                //result++;
            }
            else if(given==1&&ungiven==1){
                result++;
            }

        }

        eq=n-add-minus;


        if(s<=add){
            result+=s;
        }
        else{
            s=s-add;
            result+=add;
            if(s<=eq){
                ;
            }
            else{
                s=s-eq;
                result-=s;
            }
        }

        printf("Case #%d: %d\n",i+1,result);
    }
    return 0;
}

