#include <iostream>
#include <vector>

using namespace std;

typedef struct paire
{
    int left, right;
    paire(int l, int r)
    {
        left = l;
        right = r;
    }
} paire;

typedef struct IntraNet
{
    vector<paire> Links;

    IntraNet()
    {
        Links.clear();
    }

    int UpIntersection(paire L)
    {
        int res = 0;
        vector<paire>::iterator it;
        for (it = Links.begin();it<Links.end();it++)
        {
            if ((it->left < L.left) && (it->right > L.right))
            {
                res++;
            }
        }
        return res;
    }
} IntraNet;



int main()
{
    int T, N, X, Y;

    cin >> T;
    for (int i=1;i<=T;i++)
    {
        int res = 0;
        IntraNet Net = IntraNet();
        cin >> N;

        for (int j=0;j<N;j++)
        {
            cin >> X;
            cin >> Y;

            Net.Links.push_back(paire(X, Y));
        }

        vector<paire>::iterator it;
        for (it = Net.Links.begin();it<Net.Links.end();it++)
        {
            res += Net.UpIntersection(*it);
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 1;
}

