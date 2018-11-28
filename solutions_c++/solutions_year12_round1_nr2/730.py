#include <cstdio>
#include <algorithm>
#include <utility>
#include <set>

using namespace std;

bool comp (pair <int, int> a, pair <int, int> b){
    if (a.first < b.first){
        return true;
    }
    if (a.first == b.first && a.second > b.second){
        return true;
    }
    return false;
}

pair <int, int> levels[10001];
bool done[10001];
bool progress;
set <pair<int, int> > open;
set <pair<int, int> > candofirst;
int cases;
int numlevels;
int stars;
int indexa;
int counta;

int main(){
    scanf("%d", &cases);
    for (int i = 0; i < cases; i++){
        scanf("%d", &numlevels);
        open.clear();
        candofirst.clear();
        for (int j = 0; j < numlevels; j++){
            scanf("%d %d", &levels[j].first, &levels[j].second);
            done[j] = false;
        }
        stars = 0;
        indexa = 0;
        counta = 0;
        progress = true;
        sort(levels, levels+numlevels, comp);
        for (int j = 0; j < numlevels; j++){
            open.insert(make_pair(levels[j].second, j));
        }
        while (stars < 2*numlevels && progress){
            progress = false;
            while (open.begin() != open.end() && open.begin()->first <= stars){
//                printf ("doing second of %d\n", open.begin()->second);
                if (!done[open.begin()->second]){
                    stars += 2;
                } else {
                    stars += 1;
                }
                counta++;
                progress = true;
                done[open.begin()->second] = true;
                open.erase(open.begin());
            }
            while (indexa < numlevels && levels[indexa].first <= stars){
                candofirst.insert(make_pair(-levels[indexa].second, indexa));
                indexa++;
//                printf ("adding %d %d\n", -(levels[indexa-1].second), indexa-1);
            }
            while (candofirst.begin() != candofirst.end() && done[candofirst.begin()->second]){
//                printf ("removing %d %d\n", candofirst.begin()->first, candofirst.begin()->second);
                candofirst.erase(candofirst.begin());
            }
            if (candofirst.begin() != candofirst.end()){
                done[candofirst.begin()->second] = true;
//                printf ("doing first of %d\n", candofirst.begin()->second);
                candofirst.erase(candofirst.begin());
                stars++;
                counta++;
                progress = true;
            }
        }
        printf("Case #%d: ", i+1);
        if (stars < 2*numlevels){
            printf ("Too Bad\n");
        } else {
            printf ("%d\n", counta);
        }
    }
}
