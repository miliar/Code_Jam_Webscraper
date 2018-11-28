// http://libax.googlecode.com
#include <ax/ax_core.h>

class Q {
public:
	int64_t n;
	int t;

	axStatus onTake( Q &src ) { operator=(src); return 0; }

	axStatus toStringFormat( axStringFormat &f ) const {
		return f.format("{?}:{?}", n, t);
	}
};

static int64_t itr_c = 0;

int64_t itr( axArray<Q> &aa, size_t ai, axArray<Q> &bb, size_t bi ) {
	itr_c++;

	int64_t c = 0;
	if( ai >= aa.size() ) return c;
	if( bi >= bb.size() ) return c;

	Q oa = aa[ai];
	Q ob = bb[bi];

	Q &a = aa[ai];
	Q &b = bb[bi];

	if( a.t == b.t ) {
		int64_t mn = ax_min( a.n, b.n );
		c   += mn;
		a.n -= mn;
		b.n -= mn;
		if( a.n == 0 ) ai++;
		if( b.n == 0 ) bi++;

		int64_t d = itr( aa, ai, bb, bi );

		b = ob;
		a = oa;

		c += d;
	}else{
		int64_t dropA = itr( aa, ai+1, bb, bi   );
		int64_t dropB = itr( aa, ai  , bb, bi+1 );
		c += ax_max( dropA, dropB );
	}

	return c;
}

axStatus doCase( FILE* f, FILE* of, int t ) {
	itr_c = 0;

	axStatus st;
	int N, M;
	if( 2 != fscanf( f, "%d %d", &N, &M ) ) return -2;

	axArray<Q>	aa;
	st = aa.resize(N);		if( !st ) return st;
	for( int i=0; i<N; i++ ) {
		Q &a = aa[i];
		if( 2 != fscanf( f, "%lld %d", &a.n, &a.t ) ) return -2;
	}

	axArray<Q>	bb;
	st = bb.resize(M);		if( !st ) return st;
	for( int i=0; i<M; i++ ) {
		Q &b = bb[i];
		if( 2 != fscanf( f, "%lld %d", &b.n, &b.t ) ) return -2;
	}


	int64_t c = itr( aa, 0, bb, 0 );

	fprintf( of, "Case #%d: %lld\n", t+1, c );
	ax_print("case {?}: {?}  ({?})\n", t+1, c, itr_c );
//	ax_print("{?}\n{?}\n\n", aa, bb );

	return 0;
}

axStatus solve() {
	axStatus st;
	FILE *f = fopen("C-small-attempt1.in", "rb" );
	if( !f ) return -1;

	FILE *of = fopen("out.txt", "wb" );
	if( !of ) return -1;

	int T;
	if( 1 != fscanf( f, "%d", &T ) ) return -2;

	for( int t=0; t<T; t++ ) {
		st = doCase( f, of, t );	if( !st ) return st;
	}

	fclose(f);
	fclose(of);

	return 0;
}

int main() {
	axStopWatch	w;
	axStatus st = solve();

	ax_print("end return {?} time={?}\n", st, w.get() );

	_getch();
	return 0;
}

