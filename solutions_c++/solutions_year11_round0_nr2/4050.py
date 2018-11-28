#include <iostream>
#include <vector>

using namespace std;

struct spoj {
    char prvi;
    char drugi;
    char novi;
};

int main(void) {
    int brl;

    scanf ("%d\n", &brl);

    for (int i=0; i<brl; ++i) {
        vector < char > stog;
        vector < spoj > sp;
        vector < pair < char, char > > bris;
        char znak;

        int brsp, brbr, brzn;

        scanf ("%d", &brsp);
        sp.resize (brsp);
        for (int j=0; j<brsp; ++j) {
            scanf (" %c%c%c", &sp[j].prvi, &sp[j].drugi, &sp[j].novi);
            //printf ("%c %c %c\n", sp[j].prvi, sp[j].drugi, sp[j].novi);
        }

        //system ("pause");

        scanf ("%d", &brbr);
        bris.resize(brbr);
        char lala;
        for (int j=0; j<brbr; ++j) {
            scanf ("%c%c%c", &lala, &bris[j].first, &bris[j].second);
            //printf ("-%c- -%c-\n", bris[j].first, bris[j].second);
        }
        //system ("pause");

        scanf ("%d", &brzn);
        scanf ("%c", &lala);
        for (int j=0; j<brzn; ++j) {
            scanf ("%c", &znak);
            stog.push_back (znak);
            bool ostani = true;

            while (ostani) {
                ostani = false;
                for (int k=0; k<brsp; ++k) {
                    if (stog.size() > 1 && (stog[stog.size()-1] == sp[k].prvi && stog[stog.size()-2] == sp[k].drugi || stog[stog.size()-2] == sp[k].prvi && stog[stog.size()-1] == sp[k].drugi)) {
                        stog.pop_back();
                        stog[stog.size()-1] = sp[k].novi;
                        ostani = true;
                        break;
                    }
                }
                for (int k=0; k<brbr; ++k) {
                    for (int l=0; l<stog.size()-1; ++l)
                        if (stog.size() > 1 && (stog[l] == bris[k].first && stog[stog.size()-1] == bris[k].second
                        || stog[l] == bris[k].second && stog[stog.size()-1] == bris[k].first)) {
                            stog.clear();
                            break;
                        }
                }
            }
        }

        printf ("Case #%d: [", i+1);

        if (!stog.empty()) {
            for (int j=0; j<stog.size()-1; ++j)
                printf ("%c, ", stog[j]);
        }
        if (!stog.empty())
            printf ("%c]\n", stog[stog.size()-1]);
        else
            printf ("]\n");
    }

    return 0;
}
