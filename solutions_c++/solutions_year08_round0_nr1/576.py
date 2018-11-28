#include<iostream>
#include<map>
#include<string>

using namespace std ;

int main()
{
	map<string , bool> m , empty ;
	map<string , bool>::iterator m_i ;
	string temp ;
	char name[150] ;
	int tcase , cse , s , i , q , res , check ;

	freopen("1.txt" , "r" , stdin) ;
	freopen("2.txt" , "w" , stdout) ;

	cin >> tcase ;
	for(cse = 1 ; cse <= tcase ; cse++)
	{
		m = empty ;
		cin >> s ;
		gets(name) ;
		for(i = 0 ; i < s ; i++)
		{
			gets(name) ;
			temp = name ;
			m[temp] = 0 ;
		}
		cin >> q ;
		check = 0 ;
		res = 0 ;
		gets(name) ;
		for(i = 0 ; i < q ; i++)
		{
			gets(name) ;
			temp = name ;
			if(!m[temp])
			{
				m[temp] = 1 ;
				check++ ;
				if(check == s)
				{
					check = 1 ;
					for(m_i = m.begin() ; m_i != m.end() ; m_i++)
						m_i->second = 0 ;
					m[temp] = 1 ;
					res++ ;
				}
			}
		}
		cout << "Case #" << cse << ": " << res << "\n" ;
	}
}