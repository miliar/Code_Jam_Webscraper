#include <iostream>
#include <string>
#include <vector>
using namespace std ;

typedef struct
{
	int	ta, tb ;
	bool flag ;
}TRAIN ;

bool CMP( TRAIN a, TRAIN b )
{
	if( a.ta == b.ta )
		return a.tb < b.tb ;	
	return a.ta < b.ta ;
}


int main()
{	
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	int n, na, nb, t, cnta , cntb;
	cin >> n ;
	for( int kase = 1; kase <= n; kase ++ )
	{
		cin >> t;
		cin >> na >> nb ;
		int i, j;
		string ot, at;
		vector<TRAIN> tr;
		tr.clear();
		TRAIN temp ;
		temp.flag = false;
		for( i = 0; i < na; i ++ )
		{
			cin >> ot >> at ;
			temp.ta = ((ot[0]-'0')*10+ot[1]-'0')*60+(ot[3]-'0')*10+ot[4]-'0';
			temp.tb = ((at[0]-'0')*10+at[1]-'0')*60+(at[3]-'0')*10+at[4]-'0';
			tr.push_back(temp);	
		}
		temp.flag = true ;
		for( i = 0; i < nb; i ++ )
		{
			cin >> ot >> at ;
			temp.ta = ((ot[0]-'0')*10+ot[1]-'0')*60+(ot[3]-'0')*10+ot[4]-'0';
			temp.tb = ((at[0]-'0')*10+at[1]-'0')*60+(at[3]-'0')*10+at[4]-'0';
			tr.push_back(temp);	
		}
		sort(tr.begin() , tr.end() , CMP) ;
	
		
//		for( i = 0 ; i < tr.size() ; i ++ )
		{
//			cout << tr[i].ta << "---" << tr[i].flag << "---"<< tr[i].tb << endl ;	
		}
		
		cnta = cntb = 0 ;
		while(tr.size())
		{
			if(tr[0].flag == false)
				cnta ++ ;
			else	cntb ++ ;
			int time = tr[0].tb + t ;
			bool f = tr[0].flag ;
			i = 0 ;
			tr.erase(tr.begin()+i);
			while(1)
			{
				for(i=0; i<tr.size(); i ++ )
				{
					if(tr[i].ta >= time && tr[i].flag^f)
					{
						time = tr[i].tb + t;
						f = f^1 ;
						tr.erase(tr.begin()+i);	
						i--;
//						for( i = 0 ; i < tr.size() ; i ++ )
//						{
//							cout << "erase :"<< tr[i].ta << "---" << tr[i].flag << "---"<< tr[i].tb << endl ;	
//						}
					}	
			
				}
				if (i==tr.size())	break;
			}
				
		}
		cout<<"Case #"<<kase<<": "<<cnta<<" "<<cntb<<endl;	
	}
//    system("pause");
    return 0 ;
}
