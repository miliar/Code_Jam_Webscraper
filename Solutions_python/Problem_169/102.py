from decimal import Decimal as D
for case in range (int(input())):
	N, V, X = input().strip().split()
	N = int(N)
	V, X = D(V), D(X)

	data = [[D(x) for x in input().strip().split()] for i in range (N)]

	if N == 2 and data[0][1] == data[1][1]:
		N = 1
		data[0][0] += data[1][0]

	if N == 1:
		impossible = (X != data[0][1])
		time = V/data[0][0]
	else:
		R0, X0 = data[0]
		R1, X1 = data[1]

		t0 = D(V)*(X1-X)/(R0*(X1-X0))
		t1 = D(V)*(X-X0)/(R1*(X1-X0))

		impossible = (t0 < 0) or (t1 < 0)
		time = max(t0, t1)

	print ("Case #{}: {}".format(case+1, ("IMPOSSIBLE" if impossible else time)))