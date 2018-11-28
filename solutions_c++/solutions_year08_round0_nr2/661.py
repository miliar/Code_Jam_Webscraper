#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>

#define DEBUG						0

using namespace std;

struct SHaveTrain
{
    bool A;
    int FreeFrom;
};

struct STrain
{
    bool A;
    int Start, Stop;
};

struct lttrain
{
  bool operator()(SHaveTrain f, SHaveTrain s) const
    {
        if( f.FreeFrom == s.FreeFrom ) { return f.A; }
        return f.FreeFrom < s.FreeFrom;
    }
};

/* Sortowanie wg. Czasu odjazdu, Czasu przyjazdu */
bool __cmp_train_start(STrain f, STrain s)
{
    if( f.Start == s.Start ) { return f.Stop < s.Stop; }
    return f.Start < s.Start;
}

/* Sortowanie wg. Czasu przyjazdu, Czasu odjazdu */
/*bool __cmp_train_start(STrain f, STrain s)
{
    if( f.Stop == s.Stop ) { return f.Start < s.Start; }
    return f.Stop < s.Stop;
}*/

pair<int,int> DO_TEST(void)
{
    int i,j,k,l,m,n,t,na,nb;
    pair<int,int> R;

    STrain ST;
    SHaveTrain HT;

    vector<STrain> VT;
    multiset<SHaveTrain, lttrain> SHT;
    multiset<SHaveTrain>::iterator SHTiter;

    /* init */
    R.first = 0;
    R.second = 0;
    /* end of init */

    scanf("%d%d%d", &t, &na, &nb);

    for( i=0; i < na; i++ ) {
	scanf("%d:%d %d:%d", &k, &l, &m, &n);
	ST.A = true;
	ST.Start = k*60 + l;
	ST.Stop = m*60 + n;
	VT.insert(VT.end(), ST);
    }

    for( i=0; i < nb; i++ ) {
	scanf("%d:%d %d:%d", &k, &l, &m, &n);
	ST.A = false;
	ST.Start = k*60 + l;
	ST.Stop = m*60 + n;
	VT.insert(VT.end(), ST);
    }

    sort(VT.begin(), VT.end(), __cmp_train_start);

    if(DEBUG) for( i=0; i < VT.size(); i++ ) {
	printf("%02d:%02d %02d:%02d (%d)\n", VT[i].Start/60, VT[i].Start%60, VT[i].Stop/60, VT[i].Stop%60, (int)VT[i].A);
    }

    for( i=0 ; i < VT.size(); i++ ) {

	/* Sprawdz czy masz wolny pociag na danej stacji o tej godzinie, naliczanie wyniku jezeli pociagu nie mamy w lokomotywowni */
	if( VT[i].A ) { R.first++; } else { R.second++; }
	for( SHTiter = SHT.begin(); SHTiter != SHT.end(); SHTiter++ ) {
	
	    /* Jezeli jest wolny pociag ale na przeciwnej stacji do pomin */
	    if( SHTiter->A != VT[i].A ) { continue; }
	
	    /* Jezeli pociag bedzie dostepny pozniej, niz potrzeba */
	    if( SHTiter->FreeFrom > VT[i].Start ) { break; }
	
	    if(DEBUG) printf("Z lokomotywowni %c odjechal pociag, ktory jest wolny od %02d:%02d.\n", HT.A?'A':'B', SHTiter->FreeFrom/60, SHTiter->FreeFrom%60);
	
	    /* Wykorzystujemy pociag */
	    SHT.erase(SHTiter);
	
	    /* Odejmujemy od wyniku to co dodalismy przed wejsciem do petli */
	    if( VT[i].A ) { R.first--; } else { R.second--; }
	
	    /* Mission Complete */
	    break;
	}
	
	if(DEBUG) printf("%02d:%02d -> %02d:%02d [%c]\n", VT[i].Start/60, VT[i].Start%60, VT[i].Stop/60, VT[i].Stop%60, VT[i].A?'A':'B');

	/* Dodaj wolny pociag o godzinie Przyjazdu + Czas zmiany lokomotywy na przeciwnej stacji */
	HT.FreeFrom = VT[i].Stop + t;
	HT.A = !VT[i].A;
	SHT.insert(HT);

	if(DEBUG) printf("Lokomotywownia %c wzbogacila sie o pociag, ktory jest wolny od %02d:%02d.\n", HT.A?'A':'B', HT.FreeFrom/60, HT.FreeFrom%60);

    }

    return R;
}

int main(void)
{
    int i,j,k,l,n;
    pair<int,int> R;

    scanf("%d", &n);

    for( i=0; i < n; i++ ) {
	R = DO_TEST();
	printf("Case #%d: %d %d\n", i+1, R.first, R.second);
    }

    return 0;
}
