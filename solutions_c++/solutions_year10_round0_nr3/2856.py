

#include <iostream>
#include <tchar.h>

using namespace std ;

typedef struct {
	int index ;  // 第几趟;
	int secondindex; //第二次是第几趟 ;
	int curw  ;  // 以它为起始时的载重量; 
    bool used ;

	int cycle0w;
	int cycle1w;
} descriptor ;

static descriptor dtors[1000];
static int   cycleindex ;

int g_datas[1000] ;  // 最多1000组 
int times, maxw , gc ;
 

static int cur_header = 0 ; 

	// 存在单个小组的人数均大于车载量 ;
bool case1( int & curw)
{  
	for( int i=0; i < gc; i++ )
	{
		// 如果有单个组>maxw则停止，说明再也无法拉人了
		if ( maxw < g_datas[i] ) 
			return true ; 
		else
			curw += g_datas[i] ;
	} 
	return false ;
}

	// 一车搞定所有 ; 
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
		// 能装就装
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
	// 如果小于一天的所有次数 ，则返回 false ; 
    bool found = false ;
	cycles =0;
	for(;cycles< times;cycles++ )
	{
		if ( ! dtors[cur_header].used  )
		{
			dtors[cur_header].index =cycles ; // 第几趟; 
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
		// 说明也就拉这么多了 ;
		cout << one_cycle_w << endl ;
		return false ;
	}
	
	return true ;  
}

void case3( )
{
	// 先取得循环次数 : 多少次后，回到原始状态 ;
	bool be  = get_min_cycles( );

	if( be )
	{
		// 找到 		
		int allv = 0 ;
		allv   +=   dtors[cycleindex].cycle0w ;
		int t1 = times - dtors[cycleindex].index ;  	
		int cycles = dtors[cycleindex].secondindex - dtors[cycleindex].index  ; 
		int t = t1 / cycles ;
		allv   +=   t * ( dtors[cycleindex].cycle1w -dtors[cycleindex].cycle0w ) ;

		//剩下的再装一次 ; 
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

