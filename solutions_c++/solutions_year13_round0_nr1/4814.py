#include<fstream>
using namespace std;

ifstream fin("tictac.in");
ofstream fout("tictac.out");

int T; char q;
int xr[4], xc[4];
int yr[4], yc[4];
int xd1, xd2;
int yd1, yd2;

int main(){
    fin >> T;
    for(int t=0; t<T; t++){
        fout << "Case #" << t+1 << ": ";
        bool unf = false;
        
        for(int a=0; a<4; a++)
            xr[a] = xc[a] = yr[a] = yc[a] = 0;
            
        xd1 = xd2 = yd1 = yd2 = 0;
        
        for(int a=0; a<4; a++)
            for(int b=0; b<4; b++){
                q = '\n';
                while(q=='\n'){
                    fin >> q;
                }
                
                if(q=='.'){
                    unf = true;
                    continue;
                }
                if(q=='X' || q=='T'){
                    xr[a]++;
                    xc[b]++;
                    if(a==b) xd1++;
                    if(a+b==3) xd2++;
                }
                if(q=='O' || q=='T'){
                    yr[a]++;
                    yc[b]++;
                    if(a==b) yd1++;
                    if(a+b==3) yd2++;
                }
            }
            
        bool done = false;

        for(int a=0; a<4; a++)
            if(xr[a] == 4 || xc[a] == 4){
                if(!done) fout << "X won" << endl;
                done = true;
            }
        if(xd1==4 || xd2==4){
            if(!done) fout << "X won" << endl;
            done = true;
        }
        if(done) continue;
        
        for(int a=0; a<4; a++)
            if(yr[a] == 4 || yc[a] == 4){
                if(!done) fout << "O won" << endl;
                done = true;
            }
        if(yd1==4 || yd2==4){
            if(!done) fout << "O won" << endl;
            done = true;
        }
        if(done) continue;
        
        if(unf) fout << "Game has not completed" << endl;
        else fout << "Draw" << endl;
    }
}
