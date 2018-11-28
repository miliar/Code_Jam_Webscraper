#include <iostream>
#include <string>
using namespace std;

int main(){
    int n,c,d,t,cl,x;
    bool combed,clred;;
    cin>>t;
    for (int z=0;z<t;z++){
        string comb[40],opp[30],in,out="";
        char clr[30];
        cl=0;
        cin>>c;
        for (int y=0;y<c;y++)
            cin>>comb[y];
        cin>>d;
        for (int y=0;y<d;y++)
            cin>>opp[y];
        cin>>n;
        cin>>in;
        x=0;
        while (x<in.length()){
            combed=0;
            clred=0;
            for (int y=0;y<cl;y++){
                if (in[x]==clr[y]){
                   out="";
                   clr[y]='a';
                   clred=1;
                }
            }
            if (x<in.length()-1){
             if (!clred){
              for (int y=0;y<c;y++){
                if (in[x]==comb[y][0]){
                   if (in[x+1]==comb[y][1]){
                      out+=comb[y][2];
                      x++;
                      combed=1;
                   }
                }
                else if (in[x]==comb[y][1]){
                   if (in[x+1]==comb[y][0]){
                      out+=comb[y][2];
                      x++;
                      combed=1;
                   }
                }
              }
             }
            }
            if (!combed && !clred){
                out+=in[x];
                for (int y=0;y<d;y++){
                    if (in[x]==opp[y][0]){
                       clr[cl]=opp[y][1];
                       cl++;
                    }
                    else if (in[x]==opp[y][1]){
                       clr[cl]=opp[y][0];
                       cl++;
                    }
                }
            }
            x++;
        }
        //cout<<c<<" "<<comb[0]<<" "<<d<<" "<<opp[0]<<" "<<n<<" "<<in<<endl;
        printf("Case #%d: [",z+1);
        if (!out.empty()){
        cout<<out[0];
        for (int x=1;x<out.length();x++)
            cout<<", "<<out[x];}
        if (z<t-1)
          cout<<"]\n";
        else
          cout<<"]";
    }
    return 0;
}
