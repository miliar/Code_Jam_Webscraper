#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <list>

int n_cards;
int n_indices;
int indices[100];

int cards[5000];

void solve()
{
    scanf("%d %d", &n_cards, &n_indices);
    for (int i = 0; i < n_indices; i++)
        scanf("%d", &indices[i]);

    int count = 1;
    cards[0] = n_cards;

    int next = n_cards - 1;
    int pos = 0;
    
    while (next != 0) {
        pos = ((pos - (next % count)) + count) % count;

        for (int i = count - 1; i >= pos; i--)
            cards[i+1] = cards[i];
        count++;

        cards[pos] = next;
        next--;
    }

    for (int i = 0; i < n_indices; i++) {
        if (i > 0)
            printf(" ");
        printf("%d", cards[(indices[i] - 1 + pos) % count]);
    }

    /*
    for (int i = 0; i < count; i++)
        printf("%d ", cards[(i + pos) % count]);
    */
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

