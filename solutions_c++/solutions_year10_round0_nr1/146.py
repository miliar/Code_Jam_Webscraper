/*Problem
The Snapper is a clever little gadget that, 
on one side, plugs into a power socket and, 
on the other side, exposes a power socket 
for plugging in a light or other device.

When the Snapper is in the ON state and is receiving power from the input socket,
then the connected device is receiving power as well.
When you snap your fingers, the Snapper toggles between the ON and OFF states.
Of course, snapping your fingers only has an effect if the Snapper is plugged in and is receiving power from the socket.

In hopes of destroying the universe by means of a singularity,
I have purchased N Snapper devices and chained them together
by plugging the first one into a power socket,
the second one into the first one, and so on.
The light is plugged into the Nth Snapper.

Initially, all the Snappers are in the OFF state,
so only the first one is receiving power from the socket, and the light is off.
I snap my fingers once, which toggles the first Snapper into the ON state and gives power to the second one.
I snap my fingers again, which toggles both Snappers and then promptly cuts power off from the second one,
leaving it in the ON state, but with no power.
I snap my fingers the third time, which toggles the first Snapper again and gives power to the second one.
Now both Snappers are in the ON state, and if my light is plugged into the second Snapper it will be on.

I keep doing this for hours. Will the light be on or off after I have snapped my fingers K times?
The light is on if and only if it's receiving power from the Snapper it's plugged into.

Input
The first line of the input gives the number of test cases, T.
T lines follow. Each one contains two integers, N and K.

Output
For each test case, output one line containing "Case #x: y", 
where x is the case number (starting from 1) and y is either "ON" or "OFF", indicating the state of the light bulb.
Limits
1 �� T �� 10,000.
Small dataset

1 �� N �� 10;
0 �� K �� 100;
Large dataset

1 �� N �� 30;
0 �� K �� 10^8;
*/

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>

using namespace std;

int n, k;

void init()
{
	scanf("%d%d", &n, &k);
}

void work(int testCase)
{
	int base = 1<<n;
	int answer = k%base;
	if (answer == base - 1)
		printf("Case #%d: ON\n", testCase);
	else
		printf("Case #%d: OFF\n", testCase);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int T = 0;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		init();
		work(i+1);
	}
}