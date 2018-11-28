#include "cstdio"
#include "stack"
#include "cstring"
#include "string"
#include "iostream"

using namespace std;

int main(void)
{
    int i,j,t,mat[30][30],c,d,n,opp[30];
    int there[30];
    char buff[110];
    string b;

    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        memset(mat,-1,sizeof(mat));
        //memset(opp,28,sizeof(opp));

        for(j=0;j<30;j++)opp[j]=28;
        
        scanf("%d",&c);
        while(c--)
        {
            scanf("%s",buff);
            mat[(int)(buff[0]-'A')][(int)(buff[1]-'A')]=mat[(int)(buff[1]-'A')][(int)(buff[0]-'A')]=(int)(buff[2]-'A');
        }

        scanf("%d",&d);
        while(d--)
        {
            scanf("%s",buff);
            opp[(int)(buff[0]-'A')]=(int)(buff[1]-'A');
            opp[(int)(buff[1]-'A')]=(int)(buff[0]-'A');

            //mat[(int)(buff[0]-'A')][(int)(buff[1]-'A')]=mat[(int)(buff[1]-'A')][(int)(buff[0]-'A')]=-1;
        }

        scanf("%d",&n);
        scanf("%s",buff);
        b="";
        memset(there,0,sizeof(there));

        for(j=0;j<n;j++)
        {
            //cout << b << endl;
            c=(int)(buff[j]-'A');

            if(b=="")
            {
                b+=buff[j];
                there[c]++;
            }
            else
            {
                //printf("%d %d\n",c,opp[c]);
                
                if(mat[(int)(b[b.length()-1]-'A')][c]!=-1)
                {
                    //cout << "OK2" << endl;
                    there[(int)(b[b.length()-1]-'A')]--;
                    b[b.length()-1]=(char)(mat[b[b.length()-1]-'A'][c]+'A');
                }
                else if(there[opp[c]]!=0)
                {
                    //cout << "OK1" << endl;
                    b="";
                    memset(there,0,sizeof(there));
                }
                else
                {
                    //cout << "OK3" << endl;
                    b+=buff[j];
                    there[c]++;
                }
            }
        }

        printf("Case #%d: [",i);

        j=0;
        for(j=0;j<b.length();j++)
        {
            if(j!=0)printf(", ");

            printf("%c",b[j]);
            //b.pop();
        }
        printf("]\n");
    }

    return 0;
}
