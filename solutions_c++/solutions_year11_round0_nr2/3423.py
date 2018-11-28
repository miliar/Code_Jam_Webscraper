#include<cstdio>
#include<vector>
#include<algorithm>

struct comb
{
    char first;
    char second;

    bool operator==(const comb& other)
    {
        if((first == other.first && second == other.second) || (first == other.second && second == other.first))
            return true;
        else
            return false;
    }

    char contains(char c)
    {
        if(first == c)
            return second;
        else if(second == c)
            return first;
        else
            return 0;
    }
};

int anzcombis;
comb combis[50];
char combto[50];
int anzopps;
comb opp[50];
int n;
char str[150];

std::vector<char> board;

void solve(int T)
{
    int i,j,k;

    scanf("%d ", &anzcombis);
    for(i=0; i<anzcombis; i++)
        scanf("%c%c%c ", &combis[i].first, &combis[i].second, &combto[i]);
    scanf("%d ", &anzopps);
    for(i=0; i<anzopps; i++)
        scanf("%c%c ", &opp[i].first, &opp[i].second);
    scanf("%d ", &n);
    for(i=0; i<n; i++)
        scanf("%c", &str[i]);
    scanf("\n");

    board.push_back(str[0]);
    for(i=1; i<n; i++)
    {
        board.push_back(str[i]);

        // check for combi
        comb act;
        act.first = board[board.size()-2];
        act.second = board[board.size()-1];
        for(j=0; j<anzcombis; j++)
        {
            if(combis[j] == act)
            {
                board.pop_back();
                board.pop_back();
                board.push_back(combto[j]);
                if(i != n-1)
                    board.push_back(str[++i]);
                break;
            }
        }

        // check for opp
        for(j=0; j<anzopps; j++)
        {
            std::vector<char>::iterator it1 = std::find(board.begin(), board.end(), opp[j].first);
            std::vector<char>::iterator it2 = std::find(board.begin(), board.end(), opp[j].second);

            if(it1 != board.end() && it2 != board.end())
            {
                board.clear();
                if(i != n-1)
                    board.push_back(str[++i]);
            }
        }
    }

    printf("Case #%d: ", T);

    if(board.size() > 0)
    {
        printf("[");
        for(i=0; i<board.size()-1; i++)
            printf("%c, ", board[i]);
        printf("%c]\n", board[board.size()-1]);
    }
    else
    {
        printf("[]\n");
    }

    board.clear();
}

int main()
{
    int i, T;

    scanf("%d", &T);
    for(i=0; i<T; i++)
    {
        solve(i+1);
    }
    
    return 0;
}
