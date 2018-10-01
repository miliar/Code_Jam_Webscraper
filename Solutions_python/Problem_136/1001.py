def ptc(t, ans):
	tp = "Case #";
	tp += str(t);
	tp += ": ";
	tp += str(ans);
	print tp;

n = input();
for t in range(n):
	(cost, fbonus, target) = map(float, raw_input().split());
	rate = 2.0;
	spent = 0.0;

	currentMin = 100000000;

	while True:
		noMoreFarm = target / rate + spent;
		if(noMoreFarm > currentMin):
			break;
		currentMin = noMoreFarm;
		spent += cost / rate;
		rate += fbonus;

	ptc(t+1, currentMin);
