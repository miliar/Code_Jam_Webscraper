#include <iostream>

using namespace std;

int ncases;
int turnaround;
int na, nb;
int partidas_a[100], partidas_b[100], chegadas_a[100], chegadas_b[100], chegadas_a_used[100], chegadas_b_used[100];
int pa, pb, ca, cb;
int temqter_a, temqter_b;

int compare(const void *a, const void *b) {
    return (*(int *) b - *(int *) a);// reverse sort
}

int main() {

    int i, j, k;
    int h, m;

    cin >> ncases;

    for (i=0; i<ncases; i++) {

        cin >> turnaround >> na >> nb;
        temqter_a = na;
        temqter_b = nb;

        pa = ca = pb = cb = 0;

        for (j=0; j<na; j++) {

            scanf("%d:%d", &h, &m);
            partidas_a[pa++] = h * 60 + m;

            scanf("%d:%d", &h, &m);
            chegadas_b[cb] = h * 60 + m + turnaround;
            chegadas_b_used[cb] = 0;
            cb++;

            //cout << partidas_a[pa-1] << " - " << chegadas_b[cb-1] << endl;

        }

        for (j=0; j<nb; j++) {

            scanf("%d:%d", &h, &m);
            partidas_b[pb++] = h * 60 + m;

            scanf("%d:%d", &h, &m);
            chegadas_a[ca] = h * 60 + m + turnaround;
            chegadas_a_used[ca] = 0;
            ca++;

            //cout << partidas_b[pb-1] << " - " << chegadas_a[ca-1] << endl;

        }

        qsort(chegadas_a, ca, sizeof(int), compare);
        qsort(chegadas_b, cb, sizeof(int), compare);

        for (j=0; j<na; j++) {
            for (k=0; k<nb; k++) {
                if (partidas_a[j] >= chegadas_a[k] && chegadas_a_used[k] == 0) {
                    chegadas_a_used[k] = 1;
                    --temqter_a;
                    break;
                }
            }
        }

        for (j=0; j<nb; j++) {
            for (k=0; k<na; k++) {
                if (partidas_b[j] >= chegadas_b[k] && chegadas_b_used[k] == 0) {
                    chegadas_b_used[k] = 1;
                    --temqter_b;
                    break;
                }
            }
        }

        cout << "Case #" << i+1 << ": " << temqter_a << " " << temqter_b << endl;

        //cout << endl << "-----------------------" << endl;

    }

}
