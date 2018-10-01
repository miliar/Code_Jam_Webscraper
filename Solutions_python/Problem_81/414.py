import sys;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for case in range(T):
	N = int(f_ip.readline());

	table = [];
	WP = [];
	OWP = [];
	OOWP = [];
	
	for team in range(N):
		record = f_ip.readline().rstrip();
		table.append(record);
		wins = record.count('1');
		loss = record.count('0');
		WP.append(wins/(1.0*(wins+loss)));

	for team in range(N):
		cum_owp = 0;
		true_opponents = 0;
		for opponent in range(N):
			if table[opponent][team] != '.':
				true_opponents += 1;
				opp_record = table[opponent][:team] + '.' + table[opponent][(team+1):];
				wins = opp_record.count('1');
				loss = opp_record.count('0');
				cum_owp += wins/(1.0*(wins+loss));
		OWP.append(cum_owp*1.0/true_opponents);
		
	for team in range(N):
		cum_oowp = 0;
		true_opponents = 0;
		for opponent in range(N):
			if table[opponent][team] != '.':
				true_opponents += 1;
				cum_oowp += OWP[opponent];
				
		OOWP.append(cum_oowp*1.0/true_opponents);

			
	print "Case #" + str(case+1) + ":"
	for team in range(N):
		final = (0.25*WP[team]) + (0.5*OWP[team]) + (0.25*OOWP[team]);
		print final;