#include<iostream.h>
#include<fstream.h>
int main()
{
    ifstream f1;
    f1.open("input.in");

    ofstream f2;
    f2.open("output.txt");


    int t;
    f1>>t;
    int k=1;
    while(k<=t){
        int c;
        int d;
        int n;
        char terr[100];
        char cat[36][3];
        char dat[28][3];
        int opp[26][26];
        int comb[26][26];
        for(int i=0;i<26;i++){
        for(int j=0;j<26;j++){
                opp[i][j]=-1;
                comb[i][j]=-1;
        }
        }

        f1>>c;
        for(int i=0;i<c;i++){
            f1>>cat[i];
            comb[(int)(cat[i][0])-65][(int)(cat[i][1])-65]=(int)(cat[i][2]);
                  comb[(int)(cat[i][1])-65][(int)(cat[i][0])-65]=(int)(cat[i][2]);

        }
        f1>>d;
        for(int i=0;i<d;i++){
            f1>>dat[i];
            opp[(int)(dat[i][0])-65][(int)(dat[i][1])-65]=0;
                     opp[(int)(dat[i][1])-65][(int)(dat[i][0])-65]=0;

        }
        f1>>n;

        f1>>terr;
        char ans[100];
        int tempo=0;
        for(int i=0;i<n;i++){
            if(i==0){
                ans[tempo]=terr[i];
                tempo++;
            }
            else if(comb[(int)terr[i]-65][(int)ans[tempo-1]-65]!=-1)
            {int pos=comb[(int)terr[i]-65][(int)ans[tempo-1]-65];
                ans[tempo-1]=(char)comb[(int)terr[i]-65][(int)ans[tempo-1]-65];

            }
            else {int flag=0;
            for(int j=0;j<tempo;j++){
                if(opp[(int)terr[i]-65][(int)ans[j]-65]==0){
                    tempo=0;flag=1;
                    memset(ans, 0, sizeof(char)*100);
                break;
                }
            }
            if(flag==0){ans[tempo]=terr[i];
            tempo++;
            }

            }
        }
        f2<<"Case #"<<k<<": [";
        for(int i=0;i<tempo;i++){
            if(i!=tempo-1){
                f2<<ans[i]<<", ";
            }
            else {
                f2<<ans[i];
            }
        }
        f2<<"]\n";
    k++;
    }

}


