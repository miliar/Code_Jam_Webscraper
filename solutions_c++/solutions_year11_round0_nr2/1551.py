#include <iostream>
#include <vector>
#include <map>
using namespace std;
inline int index(char ch){
    switch (ch){
        case 'Q':
            return 0;
        case 'W':
            return 1;
        case 'E':
            return 2;
        case 'R':
            return 3;
        case 'A':
            return 4;
        case 'S':
            return 5;
        case 'D':
            return 6;
        case 'F':
            return 7;
    }
    return -1;
}
int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int c,d,n;
        cin>>c;
        char reduction[8][8];
        int cancel[8][8];
        for(int i=0;i<8;i++)
            for(int j=0;j<8;j++)
                reduction[i][j]=cancel[i][j]=0;
        char a1,a2,b,ch;
        for(int i=0;i<c;i++){
            cin>>a1>>a2>>b;
            int x=index(a1),y=index(a2);
            reduction[x][y]=reduction[y][x]=b;
        }
        cin>>d;
        for(int i=0;i<d;i++){
            cin>>a1>>a2;
            int x=index(a1),y=index(a2);
            cancel[x][y]=cancel[y][x]=1;
        }
/*        for(int i=0;i<8;i++){
            for(int j=0;j<8;j++)
                cout<<cancel[i][j]<<"\t";
            cout<<endl;
        }*/
        cin>>n;
        string clist="";
        int present[8];
        fill(present,present+8,0);
/*        for(int i=0;i<8;i++)
            cout<<present[i]<<"\t";
        cout<<endl;*/
        for(int i=0;i<n;i++){
            cin>>ch;
            int x=index(ch);
            if(x!=-1)
                present[x]++;
            int last=clist.size()-1;
            if(last>=0&&x!=-1){
                int y=index(clist[last]);
                bool flag=false;
                if(y!=-1){
                    char temp=reduction[x][y];
                    if(temp){
                        present[x]--;
                        present[y]--;
                        flag=true;
                        clist[last]=temp;
                    }
                }
                if(flag) continue;
                for(int j=0;j<8;j++)
                    if(j!=x&&cancel[x][j]&&present[j]){
                        clist.clear();
                        fill(present,present+8,0);
                        flag=true;
                        break;
                    }
                if(flag) continue;
            }
            clist+=ch;
        }
        cout<<"Case #"<<z<<": [";
        for(int i=0;i<(int)clist.size()-1;i++)
            cout<<clist[i]<<", ";
        if(clist.size())
            cout<<clist[clist.size()-1];
        cout<<"]"<<endl;
    }
    return 0;
}
