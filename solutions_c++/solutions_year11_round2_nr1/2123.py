#include <iostream>
using namespace std;

int main(){
int no;
cin>>no;
for(int i=0;i<no;i++){
    int n;
    cin>>n;
    int a[150][150];
    //int *in = new int[n];
    //for(int j=0;j<n;j++){
    //    in[j] = new int[n];
    //}
    for(int q=0;q<n;q++){
        char temp[150];
        cin>>temp;
        //cout<<temp<<endl;
        for(int p=0;p<n;p++){
            //char temp;
            //cout<<temp;
            if(temp[p] == '.'){
                a[p][q] = -1;
            }
            //if(temp == '1'){
            //a[p][q] == 1;
            //}
            //if(temp == 48){
            //    a[p][q] = 0;
            //}
            else{
                a[p][q] = (int)temp[p] - 48;
            }
        }

    }

    float wp[100][3];
    for(int l=0;l<n;l++){
        int count = 0;
        int sum = 0;
        for(int k=0;k<n;k++){
            if(a[k][l] != -1){
                count++;
                sum += a[k][l];
            }
        }
        wp[l][0] = (float)sum/count;
        wp[l][1] = sum;
        wp[l][2] = count;
    }

    float owp[100];
    for(int l=0;l<n;l++){
        float sum=0;
        float count = 0;
        for(int k=0;k<n;k++){
            if(a[k][l] != -1){
                float tem = 0;
                if(a[k][l] == 0){tem = 1;}
                sum += (wp[k][1]- tem)/(wp[k][2] -1);
                count++;
            }
        }
        owp[l] = (float)sum/count;
    }

    float oowp[100];
    for(int l=0;l<n;l++){
        float sum=0;
        float count=0;
        for(int k=0;k<n;k++){
            if(a[k][l] != -1){
                sum += owp[k];
                count++;
            }
        }
        //cout<<sum<<" "<<count<<endl;
        oowp[l] = (float)sum/count;
    }
//    cout<<a[0][0]<<a[1][0]<<a[2][0]<<endl;
//    cout<<a[0][1]<<a[1][1]<<a[2][1]<<endl;
//    cout<<a[0][2]<<a[1][2]<<a[2][2]<<endl;
    cout<<"Case #"<<i+1<<":"<<endl;
    for(int z=0;z<n;z++){
        //cout<<wp[z][0]<<" ";
        //cout<<owp[z]<<" ";
        //cout<<oowp[z]<<" ";
        cout<<0.25*wp[z][0] + 0.5*owp[z] + 0.25*oowp[z]<<endl;
    }
    //cout<<wp[0];
}
return 0;
}
