#include <iostream>
#include <queue>
using namespace std ;

#define S_LIMIT 100
#define N_LIMIT 20
#define Q_LIMIT 1000

int main()
{
    priority_queue<int, vector<int>, greater<int> > Adep, Barr, Bdep, Aarr ;
    
    unsigned int ncase, turntime, atrain, btrain ;

    unsigned int dep, deph, depm, arr, arrh, arrm, nsta, nstb ;
    
    unsigned int i, j ;
    
    scanf("%d", &ncase) ;
    //    cout << ncase << "---\n" ;
       
    for (i = 0 ; i < ncase ; ++i)
    {
	scanf("%d %d %d", &turntime, &atrain, &btrain) ;
	//	cout << turntime << "---" << atrain << "---" << btrain << "---\n" ;

	while (!Adep.empty()) Adep.pop() ;
	while (!Aarr.empty()) Aarr.pop() ;
	while (!Bdep.empty()) Bdep.pop() ;
	while (!Barr.empty()) Barr.pop() ;
	//	cout << "station a\n" ;
	for (j = atrain ; j ; --j)
	{
	    scanf("%d:%d %d:%d", &deph, &depm, &arrh, &arrm) ;
	    Adep.push(deph * 60 + depm) ;
	    Barr.push(arrh * 60 + arrm + turntime) ;
	    dep = deph * 60 + depm ;
	    arr = arrh * 60 + arrm + turntime ;
	    //	    cout << dep << "---" << arr << "---\n" ;
	}
	//	cout << "station b\n" ;
	for (j = btrain ; j ; --j)
	{
	    scanf("%d:%d %d:%d", &deph, &depm, &arrh, &arrm) ;
	    Bdep.push(deph * 60 + depm) ;
	    Aarr.push(arrh * 60 + arrm + turntime) ;
	    dep = deph * 60 + depm ;
	    arr = arrh * 60 + arrm + turntime ;
	    //	    cout << dep << "---" << arr << "---\n";
	}
	nsta = nstb = 0 ;

	while (Adep.size())
	{
	    //	    cout << Adep.top() << " " << Aarr.top() << endl;
	    if (Adep.top() < Aarr.top())
	    {
		nsta++ ;
		Adep.pop() ;
	    }
	    else
	    {
		Adep.pop() ;
		Aarr.pop() ;
	    }
	    if (!Aarr.size())
	    {
		nsta += Adep.size() ;
		break ;
	    }
	}
	
	while (Bdep.size())
	{
	    //	    cout << Bdep.top() << " " << Barr.top() << endl;
	    if (Bdep.top() < Barr.top())
	    {
		nstb++ ;
		Bdep.pop() ;
	    }
	    else
	    {
		Bdep.pop() ;
		Barr.pop() ;
	    }
	    if (!Barr.size())
	    {
		nstb += Bdep.size() ;
		break ;
	    }
	}

	printf("Case #%d: %d %d\n", i + 1, nsta, nstb) ;
    }
}
