#include <iostream>
#include <string>

using namespace std; 

int t, h, w;

int table[100][100] ,dir[100][100] , sol[100][100]; 
int move[4][2] = { {-1,0} , {0,-1} ,{0,1}, {1,0} } ; 


void recur(int a,int b,int idx) 
{
    if (sol[a][b] != -1) return ; 

    sol[a][b] = idx; 

    if (dir[a][b]!=-1) { recur(a+move[dir[a][b]][0],b+move[dir[a][b]][1],idx); }

    int k,aa,bb,min=table[a][b], ak=-1,bk;
    for(k=3;k>=0;k--) {
        aa = a+move[k][0] ; 
        bb = b+move[k][1] ; 

        if ( aa>=0 && aa<h && bb>=0 && bb<w ) {
            int aaa,bbb ; 
            if (dir[aa][bb]==-1) continue; 
            aaa = aa+move[dir[aa][bb]][0] ; 
            bbb = bb+move[dir[aa][bb]][1] ;

            if (aaa==a && bbb==b ) {
                recur(aa,bb,idx);
            }
        }
    }

}


int main() {
    int i,j,k ;
    cin >> t ;
    for(i=0;i<t ;i++) {
       cin >> h >> w ;
       for(j=0;j<h;j++) {
           for(k=0;k<w;k++) {
               cin >> table[j][k] ; 
               sol[j][k] = -1 ; 
               dir[j][k] = -1 ; 
           }
       }

       int l ;

       for(j=0;j<h;j++) {
           for(l=0;l<w;l++) {   
               int a = j, b =l ; 
               int aa,bb,min=table[a][b]-1; dir[a][b] = -1;
               for(k=3;k>=0;k--) {
                   aa = a+move[k][0] ; 
                   bb = b+move[k][1] ; 

                   if ( aa>=0 && aa<h && bb>=0 && bb<w ) {
                       if(table[aa][bb]<=min ) {
                           min = table[aa][bb] ; 
                           dir[a][b] = k; 
                       }
                   }
               }
           }
       }



       int idx = 0 ;

       for(j=0;j<h;j++) {
           for(k=0;k<w;k++) {
               if (sol[j][k]==-1) {
                   recur(j,k,idx++);
               }
           }
       }

       cout << "Case #" << i+1 << ": " << endl; 

       for(j=0;j<h;j++) {
            for(k=0;k<w;k++) {
                cout << (char)('a'+sol[j][k]) << " " ;
            }
            cout << endl;
       }
    }
    cout.flush();

    return 0 ;
}
