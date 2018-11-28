#include <cstdio>
#include <cstring>
#include <vector>
#define complement first
#define result second

using namespace std;

struct Node
{
    vector<pair<char, char> > complements;
    vector<char> neg;

    void clear()
    {
        complements.clear();
        neg.clear();
    }
};

Node A[27];
char S[105];
char E[27];
vector<char> st;

void clear()
{
    memset(E, 0, sizeof(E));
    st.clear();
}

char hasComplement(char ch)
{
    for (vector<pair<char, char> >:: iterator it = A[ch].complements.begin(); it != A[ch].complements.end(); ++it)
        if (st.size() && it->complement == st.back())
            return it->result;
    return 0;
}

int hasNegative(char ch)
{
    for (vector<char>::iterator it = A[ch].neg.begin(); it != A[ch].neg.end(); ++it)
        if (E[*it - 'A'])
            return 1;
    return 0;
}

int main()
{
    int n, c, t, d;
//	freopen("input.in", "r", stdin);
//	freopen("output.out", "w", stdout);
	scanf("%d\n", &t);
    for (int k = 1; k <= t; ++k)
    {
        scanf("%d ", &c);
        while (c--)
        {
            scanf("%s", S);
            A[S[0] - 'A'].complements.push_back(make_pair(S[1], S[2]));
            A[S[1] - 'A'].complements.push_back(make_pair(S[0], S[2]));
        }
        scanf("%d ", &d);
        while (d--)
        {
            scanf("%s", S);
            A[S[0] - 'A'].neg.push_back(S[1]);
            A[S[1] - 'A'].neg.push_back(S[0]);
        }
        scanf("%d ", &n);
        scanf("%s", S);

        for (int i = 0; i < n; ++i)
        {
            // currently analysed character
            int ch = S[i] - 'A';
            // combine elements
            char res = hasComplement(ch);
            if (st.size() && res)
            {
                --E[st.back() - 'A'];
                st.pop_back();
                st.push_back(res);
            }
            else
            {
                // check for negatives
                if (hasNegative(ch)) clear();
                else
                {
                    ++E[ch];
                    st.push_back(S[i]);
                }
            }
        }
        printf("Case #%d: [", k);
        for (unsigned int i = 0; i + 1 < st.size(); ++i)
        	printf("%c, ", st[i]);
        if (st.size()) printf("%c", st.back());
        printf("]\n");
//        for (int i = 0; i <= 25; i++)
//            if (A[i].complement || (A[i].neg))
//            {
//                if (A[i].complement) printf("%d: complement: (%c%c%c)\n", t, i + 'A', A[i].complement, A[i].result);
//                if (A[i].neg) printf("%d: neg: (%c%c)\n", t, i + 'A', A[i].neg);
//            }
        for (int i = 0; i <= 27; ++i)
            A[i].clear();
        clear();
    }

	return 0;
}
