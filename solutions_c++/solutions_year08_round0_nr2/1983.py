#include<iostream.h>
#include<conio.h>

int main() {
    int t,na,nb;
    int nc;
    cin>>nc;
    for (int zz=0;zz<nc;zz++){
    cin>>t>>na>>nb;
    char temp[5];
    int temp1;
    //cin>>temp;
    //int temp1;
    //temp1=(int)((temp[0]-'0')*1000+(temp[1]-'0')*100+(temp[3]-'0')*10+(temp[4]-'0'));
    //cout<<temp1;
    int a[210][2],b[210][2];
    for (int i=0;i<na;i++) {
        cin>>temp;
        temp1=(int)((temp[0]-'0')*1000+(temp[1]-'0')*100+(temp[3]-'0')*10+(temp[4]-'0'));
        a[i][0]=temp1;
        //cout<<temp1<<"  ";
        a[i][1]=-1;  
        cin>>temp;
        temp1=(int)((temp[0]-'0')*1000+(temp[1]-'0')*100+(temp[3]-'0')*10+(temp[4]-'0'));
        b[i][0]=temp1+t;
        //cout<<temp1<<"  ";
        b[i][1]=1;
        }
    for (int i=0;i<nb;i++) {
        cin>>temp;
        temp1=(int)((temp[0]-'0')*1000+(temp[1]-'0')*100+(temp[3]-'0')*10+(temp[4]-'0'));
        b[na+i][0]=temp1;
        //cout<<temp1<<"  ";
        b[na+i][1]=-1;  
        cin>>temp;
        temp1=(int)((temp[0]-'0')*1000+(temp[1]-'0')*100+(temp[3]-'0')*10+(temp[4]-'0'));
        a[na+i][0]=temp1+t;
        //cout<<temp1<<"  ";
        a[na+i][1]=1;
        }    
    
    int temp2;
    for(int i=0;i<na+nb;i++) {
            for (int j=0;j<na+nb-1;j++) {
                if (a[j][0]>a[j+1][0]){
                   temp2=a[j][0];
                   a[j][0]=a[j+1][0];
                   a[j+1][0]=temp2;
                   temp2=a[j][1];
                   a[j][1]=a[j+1][1];
                   a[j+1][1]=temp2;
                   }
                }
    }
    for(int i=0;i<na+nb;i++) {
            for (int j=0;j<na+nb-1;j++) {
                if (b[j][0]>b[j+1][0]){
                   temp2=b[j][0];
                   b[j][0]=b[j+1][0];
                   b[j+1][0]=temp2;
                   temp2=b[j][1];
                   b[j][1]=b[j+1][1];
                   b[j+1][1]=temp2;
                   }
                }
    }
   /*for (int i=0;i<na+nb;i++) {
         cout<<a[i][0]<<"  "<<a[i][1]<<"           "<<b[i][0]<<"  "<<b[i][1]<<endl;
         }
 cout<<endl<<endl;*/
 
    for (int i=0;i<na+nb-1;i++) {
        if  ((a[i][0]==a[i+1][0]) && (a[i][1]== -1) && (a[i+1][1]== 1)) {
            temp2=a[i][1];
                   a[i][1]=a[i+1][1];
                   a[i+1][1]=temp2;
        }
    }
    for (int i=0;i<na+nb-1;i++) {
        if  ((b[i][0]==b[i+1][0])&& (b[i][1]== -1) && (b[i+1][1]== 1)) {
            temp2=b[i][1];
                   b[i][1]=b[i+1][1];
                   b[i+1][1]=temp2;
        }
    }
 /*    for (int i=0;i<na+nb;i++) {
         cout<<a[i][0]<<"  "<<a[i][1]<<"           "<<b[i][0]<<"  "<<b[i][1]<<endl;
        }*/
    int countA =0, countB=0;
    
    int temp5=0;
    for (int i=0;i<na+nb;i++)
        {
             temp5+=a[i][1];
             if (temp5<0) {
                countA++;
                temp5=0;
             }
        }  
    temp5=0;
    
    for (int i=0;i<na+nb;i++)
        {
             temp5+=b[i][1];
             if (temp5<0) {
                countB++;
                temp5=0;
             }
        }
    
    cout<<"Case #"<<zz+1<<": "<<countA<<" "<<countB<<endl;
    }
    getch();
}
