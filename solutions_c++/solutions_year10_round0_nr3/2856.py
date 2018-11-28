

#include <iostream>
#include <tchar.h>

using namespace std ;

typedef struct {
	int index ;  // �ڼ���;
	int secondindex; //�ڶ����ǵڼ��� ;
	int curw  ;  // ����Ϊ��ʼʱ��������; 
    bool used ;

	int cycle0w;
	int cycle1w;
} descriptor ;

static descriptor dtors[1000];
static int   cycleindex ;

int g_datas[1000] ;  // ���1000�� 
int times, maxw , gc ;
 

static int cur_header = 0 ; 

	// ���ڵ���С������������ڳ����� ;
bool case1( int & curw)
{  
	for( int i=0; i < gc; i++ )
	{
		// ����е�����>maxw��ֹͣ��˵����Ҳ�޷�������
		if ( maxw < g_datas[i] ) 
			return true ; 
		else
			curw += g_datas[i] ;
	} 
	return false ;
}

	// һ���㶨���� ; 
bool case2(int &all )
{
	for(int i=0;i<gc;i++)
		  all += g_datas[i] ;

	if( all <= maxw )
		return true;
	return false ;
}


int load_one_time( )
{
	int curw = 0 ;
	int keep_header = cur_header;  
	do 
	{
		// ��װ��װ
		if( maxw >= curw + g_datas[cur_header] )
		{	
			curw += g_datas[cur_header]; 
			cur_header ++ ;
			cur_header = cur_header % ( gc ) ; 
		}
		else 
			break ;
	} 
	while( cur_header != keep_header ) ; 
	return curw ;
}


bool get_min_cycles()
{
	int cycles;
	int one_cycle_w = 0 ;
	// ���С��һ������д��� ���򷵻� false ; 
    bool found = false ;
	cycles =0;
	for(;cycles< times;cycles++ )
	{
		if ( ! dtors[cur_header].used  )
		{
			dtors[cur_header].index =cycles ; // �ڼ���; 
			dtors[cur_header].curw  = one_cycle_w ;
			dtors[cur_header].used = true ;
			dtors[cur_header].cycle0w = one_cycle_w ;
			one_cycle_w += load_one_time( );
		} 
		else 
		{ 
			dtors[cur_header].secondindex  = cycles ;
			dtors[cur_header].cycle1w = one_cycle_w ;

			cycleindex = cur_header ;
			found = true ;
			break ;
		}
	}

	if( ! found )
	{
		// ˵��Ҳ������ô���� ;
		cout << one_cycle_w << endl ;
		return false ;
	}
	
	return true ;  
}

void case3( )
{
	// ��ȡ��ѭ������ : ���ٴκ󣬻ص�ԭʼ״̬ ;
	bool be  = get_min_cycles( );

	if( be )
	{
		// �ҵ� 		
		int allv = 0 ;
		allv   +=   dtors[cycleindex].cycle0w ;
		int t1 = times - dtors[cycleindex].index ;  	
		int cycles = dtors[cycleindex].secondindex - dtors[cycleindex].index  ; 
		int t = t1 / cycles ;
		allv   +=   t * ( dtors[cycleindex].cycle1w -dtors[cycleindex].cycle0w ) ;

		//ʣ�µ���װһ�� ; 
		int remain_times = t1 % cycles ;
		for(size_t ii=0;ii< remain_times;ii++ )
		{
			allv += load_one_time( ); 
		}

		cout << allv << endl ;
	}


	return ; 
	
}

int main( )
{
	int t ; 
	cin  >> t ;
	for( int kk =0; kk<t;kk++ )
	{ 
		if( kk == 4 ) 
		{
			int debug = 0;
		}
		cycleindex == -1 ;
		for( int m=0;m<1000;m++)
			dtors[m].used = false  ; 

		cur_header = 0 ;
		cin >> times >> maxw >> gc ;
		for( int i=0;i<gc;i++)
			cin >> g_datas[i]  ;

	
		cout << "Case #" << kk+1 << ": " ;
		
		
		int all =0 ; 
		if ( case1( all ) )
		{ 
			cout << all << endl ;
			continue ;
		} 
		all = 0 ;
		if(  case2(all) )
		{
			cout << all * times << endl ;
			continue; 
		}
		
		case3( );
	}
	return 0;
}

