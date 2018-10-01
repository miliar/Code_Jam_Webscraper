
import codecs

class Problem( object ):

	def __init__( self, farmCost, farmProd, numberForWin ):

		self.farmCost = farmCost
		self.farmProd = farmProd
		self.numberForWin = numberForWin
		self.currentProd = 2.0
		self.currentSec = 0.0
		self.minResult = self.numberForWin / self.currentProd

	def update( self, val ):

		if val >= self.minResult:
			return

		self.minResult = val

	def step( self ):

		while self.currentSec < self.minResult:

			time_to_buy_farm = self.farmCost / self.currentProd
			time_to_win = self.numberForWin / self.currentProd
			self.update( self.currentSec + time_to_win )
			self.currentProd += self.farmProd
			self.currentSec += time_to_buy_farm

			# print self.currentSec, self.currentProd, self.minResult

		return self.minResult

i = 0
for line in codecs.open( 'input.in', 'r' 'utf-8' ).readlines()[1:]:
	C, F, X = map( float, line.split() )
	p = Problem( C, F, X )
	i += 1
	print 'Case #%d: %f' % ( i, p.step() )
