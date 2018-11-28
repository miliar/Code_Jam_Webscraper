

using namespace std ;
#include <iostream> 


int main( )
{
	int n , k ; 

	int c; 
	cin >> c ;
	for(int i=0;i<c;i++)
	{
		
		cin >> n >> k; 


		if ( n > k )
		{
			cout << "Case #" << i+1 << ": OFF" << endl;  
			continue ; 
		}

		// n�ھ���cycle�κ󣬻ظ���ԭʼ״̬��
		int cycle = 1<<n ;

		if( k > cycle )
			k = k % cycle ; 
		
		bool be = true ;
		int j=0 ;
		int kbegin = 0;
		for( ;j<n;j++)
		{
			//  
			int ksize = k-kbegin; 

			int kstep  = 1<<j; 
			kbegin += kstep ;

			//
			if ( kbegin > k ||  0 ==   (ksize/kstep & 1) )   //   ksize/kstep �����������˵��������ڵĵ�Դ�е磬 ż������û�е�
			{
				be = false ;
				break ;
			}
		}

		if(  !be  )
			cout << "Case #" << i+1 << ": OFF" << endl; 
		else 
			cout << "Case #" << i+1 << ": ON" << endl; 
	}
	return 0;
}

