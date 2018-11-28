#include <iostream.h>
#include <conio.h>
int main() {
    char tempo[10];
    char engine[110][101];
    char list[1010][101];
    int num_e, temp=0;
    int listN;
    int tc;
    cin>>tc;
    for (int z=0;z<tc;z++){
        cin>>num_e;
     //   cout<< "  nume " <<num_e;  
        cin.getline(tempo,10);
    for (int i=0;i<num_e;i++) {
        cin.getline (engine[i],50);
      //  cout<<engine[i]<< "  ~~  " ;
        }
    
    cin>>listN;     
    cin.getline(tempo,10);
    //cout<<" linstntstnt " << listN;  
    for (int i=0;i<listN;i++){
        cin.getline (list[i],50);
        
        }
    int flag[100];
    for (int i=0;i<num_e;i++)
        flag[i]=0;
        
    int count=0;
    int last;
    for (int i=0;i<listN;i++){
     
        for (int j=0;j<num_e;j++)
        if (!strcmp(engine[j],list[i])) {
           flag[j]=1;
           last=j;
           }
           
        temp=1;
        for(int j=0;j<num_e;j++)
                temp=temp*flag[j];
        if (temp==1) {
           count++;
           for (int k=0;k<num_e;k++)
               flag[k]=0;
           flag[last]=1;
           }
   
        }
      // cout<<"gadbad\n";
    cout<<"Case #"<<z+1<<": "<<count<<endl;
    }
    getch();
   
}

