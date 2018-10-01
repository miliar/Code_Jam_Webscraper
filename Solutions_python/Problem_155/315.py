def AmigosInvitados(S,Smax):
	SumaAcumulada = S[0]
	NumeroDeAmigos = 0
	for i in range(1,Smax+1):
		if(SumaAcumulada>=i):
			SumaAcumulada += S[i]
		else:
			NumeroDeAmigos += 1
			SumaAcumulada += S[i]+1
	return NumeroDeAmigos
T = int(input())
for i in range(T):
	Linea = input()
	LineaSeparada = Linea.split()
	Smax = int(LineaSeparada[0])
	S = [int(j) for j in list(LineaSeparada[1])]
	print("Case #%d: %d"%(i+1,AmigosInvitados(S,Smax)))