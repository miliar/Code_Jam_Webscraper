import sys;
def gcd( a ,b ):
	if b == 0 :
		return a;
	else:
		return gcd(b,a%b);
x=input();
cases = 1;
for i in range(int(x)):
	V = raw_input()
	V = V.split(' ')
	V=V[1:len(V)]; #! It has string
	MainListSize = len(V);
	for j in range(0,MainListSize):
		V[j] = int( V[j]);
	V.sort();
	l=[]; #!List Has integers
	for j in range(0,int(MainListSize)-1):
		l.append(V[j+1]-V[j]);

	ModifiedListSize = len(l);
	startGcd = 0 ;
	if ModifiedListSize == 1 :
		startGcd = l[0];
	else:
		startGcd = gcd ( l[1] , l[0] );
		for j in range( 2 , ModifiedListSize):
			TempGcd = gcd ( int(startGcd) , l[j] );
			startGcd = TempGcd ;
	T = int(startGcd);
	if (V[0]%T) ==0:
		RequiredNumber = 0;
	else:
		RequiredNumber = T-(V[0]%T);
	print "Case #%d: %d" %( cases,RequiredNumber ) ;
	cases=cases+1;
		

								

		
	





