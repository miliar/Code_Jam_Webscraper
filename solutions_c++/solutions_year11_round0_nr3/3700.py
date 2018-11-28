#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

long long total = 0;
long long maxi = -1;
//vector de bool per definir les 2 piles. Les bosses marcades amb 1 i 0 son les 2 diferents piles.

//vector <vector <bool > > memo;


long long rec(vector <long long>& v, vector <bool>& vis, long long cont){
     long long a = 0, b = 0, c = 0, d = 0;
     
     for (long long i = 0; i < v.size(); i++){
         if (vis[i]==false) { a = a^v[i]; c+=v[i]; }
         else { b = b^v[i]; d+=v[i]; }
     }
     
     //fout <<a<<" "<<b<<endl;
     
     if (cont == v.size()){
        if (a==0 or b==0) return -1;
        //fout <<a<<" "<<b<<endl;
        if (a==b) return max(c, d);
        return -1;
     }
     

     vis[cont] = true;
     maxi = max(maxi, rec(v, vis, cont+1));
     vis[cont] = false;
     maxi = max(maxi, rec(v, vis, cont+1));
     
     return maxi;
     
}

int main(){
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    long long c;
    fin >>c;
    for (long long d = 0; d < c; d++){
        long long n;
        total = 0;
        fin >>n;
        vector <long long> v(n);
        for (long long i = 0; i < n; i++) { fin >>v[i]; total+=v[i]; }
        vector <bool> vis (n, false);
        maxi = -1;
        fout <<"Case #"<<d+1<<": ";
        long long res = rec(v, vis, 0); 
        if (res!=-1) fout <<res;
        else fout <<"NO";
        fout <<endl;
        
    }
    fin >>c;
}
