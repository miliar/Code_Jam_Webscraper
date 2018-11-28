#include<iostream.h>
#include<conio.h>
#include<fstream.h>

int main()
{

    ifstream f1;
    f1.open("input.txt");
    ofstream f2;
    f2.open("output.txt");

    int t;
    f1>>t;
    int k=1;
    while(t--)
    {

        int n;
        f1>>n;
        char arr[100][100];
        double with[100][100];
        int ng[100];int totmat=0;
        double totwpi=0;
        double wp[100],win[100];
        int totwon=0;
        for(int i=0;i<n;i++){
            ng[i]=0;
            wp[i]=0;
            win[i]=0;
            for(int j=0;j<n;j++)
            {
                f1>>arr[i][j];
         if(arr[i][j]=='1')
         {wp[i]++;
         win[i]++;
         ng[i]++;
                totwon++;
         totmat++;
         }
         if(arr[i][j]=='0')

         {
             ng[i]++;
             totmat++;
         }


            }
            wp[i]=(double)(wp[i]/ng[i]);
            totwpi+=wp[i];
        }

        for(int i=0;i<n;i++){

            for(int j=0;j<n;j++){
                if(i!=j){
            if(arr[i][j]=='.'){
            with[i][j]=wp[i];}
            else if(arr[i][j]=='1'){
                with[i][j]=(double)(win[i]-1)/(ng[i]-1);
            }
            else{
            with[i][j]=(double)(win[i])/(ng[i]-1);

            }


            }

            }
            }

            double op[100];
            for(int i=0;i<n;i++){
                op[i]=0;int sum=0;
                for(int j=0;j<n;j++){
                    if(j!=i&&arr[j][i]!='.'){
                        sum++;
                        op[i]+=with[j][i];

                    }
                }
                op[i]=(double)op[i]/sum;

            }




            double rpi[100];
        f2<<"Case #"<<k<<":\n";

        for(int i=0;i<n;i++){
            rpi[i]=(double)((0.25)*wp[i])+(double)((0.50)*op[i]);
        double oop=0;int sum=0;
        for(int j=0;j<n;j++){
            if(j!=i&&arr[i][j]!='.'){
                oop+=op[j];
                sum++;
            }
        }

        oop=(double)oop/sum;
        rpi[i]+=(double)((0.25)*oop);
        f2<<rpi[i]<<"\n";

        }
        k++;
    }
}
