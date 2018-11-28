    //Other Includes
    #include<string>
    #include<iostream>
    #include<cstring>
    #include<cstdlib>
    #include<cstdio>
    #include<cmath>
    using namespace std;

    // Input macros
    #define s(n)                  scanf("%d",&n)
    #define sc(n)                 scanf("%c",&n)
    #define sl(n)                 scanf("%lld",&n)
    #define sf(n)                 scanf("%lf",&n)
    #define ss(n)                 scanf("%s",n)

  // Output Macros
  #define p(n)          printf("%d\n",n)
  #define pnl           printf("\n")

    // Useful constants
    #define INF                   (int)1e9
    #define EPS                   1e-9

    // Useful hardware instructions
    #define bitcount              __builtin_popcount
    #define gcd                   __gcd


    // Useful container manipulation / traversal macros
    #define forall(i,a,b)         for(int i=a;i<b;i++)
    #define foreach(v, c)         for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
    #define all(a)                a.begin(), a.end()
    #define in(a,b)               ( (b).find(a) != (b).end())
    #define pb                    push_back
    #define fill(a,v)             memset(a, v, sizeof a)
    #define sz(a)                 ((int)(a.size()))
    #define mp                    make_pair


    // Some common useful functions
    #define checkbit(n,b)                ( (n >> b) & 1)
    #define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
    #define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

    char a[4][4];
    /*Main code begins now */
    int checkArr(){
        // int s = 1;
        forall(i,0,4){
            if( (a[i][0]==a[i][1]) && (a[i][1]==a[i][2]) && (a[i][2]==a[i][3]) ){
                // p(s);
                if(a[i][0]=='X'){ return 0;}
                else if(a[i][0] == 'O'){ return 1;}
            }
        }
        forall(i,0,4){
            if( (a[0][i]==a[1][i]) && (a[1][i]==a[2][i]) && (a[2][i]==a[3][i]) ){
                // s=2;p(s);
                if(a[0][i]=='X'){ return 0;}
                else if(a[0][i] == 'O'){ return 1;}
            }
        }
        if( (a[0][0]==a[1][1]) && (a[1][1]==a[2][2]) && (a[2][2]==a[3][3]) ){
                // s=3;p(s);
                if(a[0][0]=='X'){ return 0;}
                else if(a[0][0] == 'O'){ return 1;}
        }
        if( (a[0][3]==a[1][2]) && (a[1][2]==a[2][1]) && (a[2][1]==a[3][0]) ){
                // s=4;p(s);
                if(a[0][3]=='X'){ return 0;}
                else if(a[0][3] == 'O'){ return 1;}
        }
        return -1;
    }

    int solve(int tcase){
        bool empty = false;
        int ti = -1,tj = -1,resi = -1;

        forall(i,0,4){
            forall(j,0,4){
                cin>>a[i][j];
                if(a[i][j] == '.'){ empty = true;  }
                else if(a[i][j] == 'T'){ ti = i,tj = j; }
            }
        }

        if(ti != -1){
            a[ti][tj] = 'X';
            resi = checkArr();
            if(resi != -1){
                return resi;
            }
            a[ti][tj] = 'O';
        }
        resi = checkArr();

        if(resi == -1){
            if(empty ){ resi = 3; }
            else { resi = 2; }
        }
        return resi;
  }
    int main()
    {
        int tcase,i=0;
        cin>>tcase;
        string result[4] = {"X won", "O won", "Draw","Game has not completed" };
        while(i<tcase){
            i++;
            cout<<"Case #"<<i<<": "<<result[solve(i)]<<"\n";
        }
    return 0;
    }
