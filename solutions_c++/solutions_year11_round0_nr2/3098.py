#include<iostream>

using namespace std;

FILE *fin=freopen("B-small-attempt3.in","r",stdin);
FILE *fout=freopen("probB.out","w",stdout);

char comb[26][26];
int opp[26][26];

void read_combine(int C) {
    for(int i=0;i<C;i++) {
        char c1,c2,r;
        cin>>c1>>c2>>r;
        comb[c1-'A'][c2-'A']=r;
        comb[c2-'A'][c1-'A']=r;
        cin.get();
    }
}

void read_opposed(int D) {
    for(int i=0;i<D;i++) {
        char c1,c2;
        cin>>c1>>c2;
        opp[c1-'A'][c2-'A']=1;
        opp[c2-'A'][c1-'A']=1;
        cin.get();
    }
}

char check(char c, char c1) {
    return comb[c-'A'][c1-'A'];
}

int curropp[8];
char opplist[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

void add_to_curr_opposed(char c,int vpos) {
    for(int i=0;i<8;i++) {
        if(c==opplist[i]) {
            curropp[i]=vpos;
            return;
        }
    }

}

void remove_from_curr_opposed(char c) {
    for(int i=0;i<8;i++) {
        if(c==opplist[i]) {
            curropp[i]=0;
            return;
        }
    }
}

void clear_curropp() {
    for(int i = 0; i<8;i++)
        curropp[i] = 0;
}


void init() {
    clear_curropp();
    for(int i=0;i<26;i++) {
         for(int j=0;j<26;j++) {
            comb[i][j]='\0';
         }
    }
    for(int i=0;i<26;i++) {
         for(int j=0;j<26;j++) {
            opp[i][j]=0;
         }
    }
}

int main() {
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        init();
        int C,D,N;
        cin>>C;
        read_combine(C);
        cin>>D;
        read_opposed(D);
        cin>>N;
        int p=0;
        char res[101];
        for(int j=0;j<N;j++) {
            char c;
            cin>>c;
            res[p++]=c;
            add_to_curr_opposed(c,p);
            char t='\0';
            if(p-2>=0)
                t = check(c,res[p-2]);
            if(t) {
                remove_from_curr_opposed(c);
                char c2=res[p-2];
                remove_from_curr_opposed(res[p-2]);
                for(int k=p-3;k>=0;k--)
                    if(c2==res[k]) {
                        add_to_curr_opposed(c2,k+1);
                        break;
                    }
                p--;
                res[p-1]=t;
            } else {
                for(int k = 0; k<8;k++) {
                    if(curropp[k]!=0 && curropp[k]!=p)
                    {
                        int l=curropp[k]-1;
                        if(opp[res[l]-'A'][c-'A']) {
                            p=0;
                            clear_curropp();
                            break;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<(i+1)<<": [";
        for(int j=0;j<p-1;j++) {
            cout<<res[j]<<", ";
        }
        if(p>0)
            cout<<res[p-1];
        cout<<"]\n";
    }
    return 0;
}
