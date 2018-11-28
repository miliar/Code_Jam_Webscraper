#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int cases, cont = 1;
    cin>>cases;
    while(cases--)
    {
        int r, c;
        cin>>r>>c;
        vector< vector<char> > tiles(r);
        for(int i=0;i<r;++i)
            for(int j=0;j<c;++j)
            {
                char k;
                cin>>k;
                tiles[i].push_back(k);
                if(i != 0 && j!= 0 && k == '#' && tiles [i-1][j] == '#'&& tiles [i-1][j-1] == '#' && tiles [i][j-1] == '#')
                {
                    tiles [i][j] = '/';
                    tiles [i][j-1] = '\\';
                    tiles [i-1][j] = '\\';
                    tiles [i-1][j-1] = '/';
                }
            }
        bool flag = true;
        for(int i=0;i<r && flag;++i)
            for(int j=0;j<c;++j)
                if(tiles[i][j] == '#')
                {
                    cout<<"Case #"<<cont<<": \nImpossible"<<endl;
                    flag = false;
                    break;
                }
        if(flag)
        {
            cout<<"Case #"<<cont<<":"<<endl;
            for(int i=0;i<r;++i)
            {
                for(int j=0;j<c;++j)
                    cout<<tiles[i][j];
                cout<<endl;
            }
            
        }
        ++cont;
    }
    return 0;
}
