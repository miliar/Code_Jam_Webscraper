
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int min3(int a, int b, int c)
{
    return (a<b)?((a<c)?a:c):((b<c)?b:c);
}

int mmin(int a1, int a2, int b1, int b2, int c1, int c2, int x1, int x2, int x3 )
{
    int avalid = !(a1<0 || a2<0);
    int bvalid = !(b1<0 || b2<0);
    int cvalid = !(c1<0 || c2<0);
    if( !avalid || !cvalid || !bvalid )
    {
        if( !avalid && !bvalid && !cvalid ) return -1;
        
        return min3( avalid?a1+a2+1-x1:1000000, bvalid?b1+b2+1-x2:1000000, cvalid?c1+c2+1-x3:1000000);
    }
    else
    {
        return min3(a1+a2+1-x1, b1+b2+1-x2, c1+c2+1-x3);
    }
}

int get_min(vector<int> tree, vector<int> gates, vector<int> change, int x, int v)
{
    if( x >= (tree.size()-1)/2 )
    {
        if( v == tree[x] ) return 0;
        else return -1;
    }
    
    int node = x+1;
    int a1 = get_min(tree, gates, change, 2*node-1, 1);
    int a2 = get_min(tree, gates, change, 2*node-1, 0);
    
    int b1 = get_min(tree, gates, change, 2*node, 1);
    int b2 = get_min(tree, gates, change, 2*node, 0);
    
    if( v == 1 )
    {
        if( gates[x] == 1 )
        {
            if( change[x] )
            {
                return mmin(a1, b1, a1, b2, a2, b1, 1, 0, 0);
            }
            else
            {
                return mmin(a1, b1, -1, -1, -1, -1, 1, 0, 0);
            }
        }
        else
        {
            return mmin(a1, b1, a1, b2, a2, b1, 1, 1, 1);
        }
    }
    else
    {
        if( gates[x] == 0 )
        {
            if( change[x] )
            {
                return mmin(a2, b2, a1, b2, a2, b1, 1, 0, 0);
            }
            else
            {
                return mmin(a2, b2, -1, -1, -1, -1, 1, 0, 0);
            }
        }
        else
        {
            /*cout << "x = " << x << endl;
            cout << "a1 = " << a1 << endl;
            cout << "a2 = " << a2 << endl;
            cout << "b1 = " << b1 << endl;
            cout << "b2 = " << b2 << endl;*/
            return mmin(a2, b2, a1, b2, a2, b1, 1, 1, 1);
        }
    }
}


int main(int argc, char **argv)
{
    int N;
    char file[50] = "output.txt";
    
    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(file);
    
    input >> N;
    
    for( int CASE = 1; CASE <= N; CASE++ )
    {
         int M, V;
         input >> M >> V;
                  
         vector<int> tree(M, 0);
         vector<int> gates(M, 0);
         vector<int> change(M, 0);
         
         for( int i = 0; i < (M-1)/2; i++ )
         {
              int G, C;
              input >> G >> C;
              
              gates[i] = G;
              change[i] = C;
         }
         
         for( int i = (M-1)/2; i < M; i++ )
         {
              int I;
              input >> I;
              
              tree[i] = I;
         }
         
         int a = get_min(tree, gates, change, 0, V);
         
         if( a>= 0 )
             output << "Case #" << CASE << ": " << a << "\n";
         else
             output << "Case #" << CASE << ": IMPOSSIBLE\n";
    }
    output.close();

    system("pause");

    return 0;
}
