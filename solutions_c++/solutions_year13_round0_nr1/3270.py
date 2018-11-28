#include<iostream>

using namespace std;
int main()
{
    int T;
    int r_x,r_o,c_x,c_o,dot,d1_x,d2_x,d1_o,d2_o,flag;
    int ar[4][4];
    char line[4];
    
    cin>>T;
    for(int I=1;I<=T;I++)
    {

        for(int i=0;i<4;i++)
        {
            cin>>line;
            //cout<<line<<endl;
            for(int j=0;j<4;j++)
            {
                if(line[j]=='X')ar[i][j]=1;
                if(line[j]=='O')ar[i][j]=2;
                if(line[j]=='T')ar[i][j]=3;
                if(line[j]=='.')ar[i][j]=4;
            }

        }
        dot=0;flag=0;d1_x=0;d2_x=0;d1_o=0;d2_o=0;
        for(int i=0;i<4;i++)
        {
        				r_x=0;r_o=0;c_x=0;c_o=0;
            for(int j=0;j<4;j++)
            {
                if(ar[i][j]==1) r_x++;
                else if(ar[i][j]==2) r_o++;
                else if(ar[i][j]==3) {r_x++;r_o++;}
                else if(ar[i][j]==4) dot++;
                
                if(ar[j][i]==1) c_x++;
                else if(ar[j][i]==2) c_o++;
                else if(ar[j][i]==3) {c_x++;c_o++;}
                
                
                
            }//cout<<endl<<"r_x:"<<r_x<<endl<<"r_o:"<<r_o<<endl<<"c_x:"<<c_x<<endl<<"c_o:"<<c_o<<endl<<"d1_x:"<<d1_x<<endl<<"d2_x:"<<d2_x<<endl;
            if(r_x==4 || c_x==4){cout<<"Case #"<<I<<": X won"<<endl;flag=1;break;}
            else if(r_o==4 || c_o==4){cout<<"Case #"<<I<<": O won"<<endl;flag=1;break;}
            
            if(ar[i][i]==1) d1_x++;
            else if(ar[i][i]==2) d1_o++;
            else if(ar[i][i]==3) {d1_x++;d1_o++;}
                
            if(ar[3-i][i]==1) d2_x++;
            else if(ar[3-i][i]==2) d2_o++;
            else if(ar[3-i][i]==3) {d2_x++;d2_o++;}
        }    //cout<<endl<<"r_x:"<<r_x<<endl<<"r_o:"<<r_o<<endl<<"c_x:"<<c_x<<endl<<"c_o:"<<c_o<<endl<<"d1_x:"<<d1_x<<endl<<"d2_x:"<<d2_x<<endl;
        if(!flag)
        {
        		if(d1_x==4 || d2_x ==4)cout<<"Case #"<<I<<": X won"<<endl;
        		else if(d2_o==4 || d1_o==4) cout<<"Case #"<<I<<": O won"<<endl;
        		else if(dot) cout<<"Case #"<<I<<": Game has not completed"<<endl;
        		else cout<<"Case #"<<I<<": Draw"<<endl;
        }
       }
}
